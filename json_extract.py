import json

with open("Product.json", "r") as file:
    python_data = json.load(file)

print(python_data["id"])
print(python_data["title"])
print(python_data["description"])