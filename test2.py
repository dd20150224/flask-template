import os

stores = {
    "store1": {"name": "Store 1", "location": "Wan Chai", "employees": 5},
    "store2": {"name": "Store 2", "location": "Central", "employees": 10},
}

url = os.getenv("DATABASE_URL", "sqlite:///data.db")
print(url)

abc = "sdfds"

if abc:
    print("abc is here")
else:
    print("abc is false")
# print(stores.values())
# print(list(stores.values()))
