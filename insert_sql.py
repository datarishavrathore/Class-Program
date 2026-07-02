import json
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",      
    database="9est"       
)

cursor = conn.cursor()

# Read JSON file
with open("Product.json", "r") as file:
    data = json.load(file)

# Insert query
query = """
INSERT INTO product
(id, title, description, category, price, discountPercentage, rating, stock)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# Values
values = (
    data["id"],
    data["title"],
    data["description"],
    data["category"],
    data["price"],
    data["discountPercentage"],
    data["rating"],
    data["stock"]
)

# Execute query
cursor.execute(query, values)

# Save changes
conn.commit()

print("Data Inserted Successfully!")

# Close connection
cursor.close()
conn.close()