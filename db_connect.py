import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="9est"
)

print("Connected Successfully")

conn.close()

import json

with open("Product.json", "r") as file:
    print(file.read())