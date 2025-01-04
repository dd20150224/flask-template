from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import StoreModel
from schemas import ItemSchema, StoreSchema

blp = Blueprint("Stores", __name__, description="Operations on stores")


@blp.route("/stores/<int:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Stor deleted."}


@blp.route("/stores")
class StoreList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        print("before: store:", store.__dict__.items())
        for key, value in store.__dict__.items():
            print(f"{key}: {value}")
        # print(f"before: store.name: {store.name}")
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A store with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the store.")

        print("after: store:", store.__dict__.items())
        for key, value in store.__dict__.items():
            print(f"{key}: {value}")
        # print(f"after: store.id = {store.name}")
        return store
