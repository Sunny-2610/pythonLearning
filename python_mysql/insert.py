import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)

cursor = conn.cursor()

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
data = ("Sunny", 20)

cursor.execute(sql, data)
conn.commit()

print("Data inserted")

cursor.close()
conn.close()
