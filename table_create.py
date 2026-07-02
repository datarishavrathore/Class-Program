import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="9est"      
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS product(
    id INT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    category VARCHAR(100),
    price DECIMAL(10,2),
    discountPercentage DECIMAL(5,2),
    rating DECIMAL(3,2),
    stock INT
)
""")

conn.commit()
print("Table Created Successfully")

cursor.close()
conn.close()