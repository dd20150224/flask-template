docker stop flask-api-app
docker build --tag flask-api .
docker run --rm -dp 5000:5000 -v %cd%:/app --name flask-api-app flask-api