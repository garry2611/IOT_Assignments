
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

query = "select * from empinfo;"

cursor = connection.cursor()

cursor.execute(query)

records = cursor.fetchall()     #   returns list of tuples

print(records)

cursor.close()

connection.close()