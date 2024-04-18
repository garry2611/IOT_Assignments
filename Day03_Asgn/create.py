
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

empid = int(input(" Enter empid : "))
name = input(" Enter name : ")
dept = input(" Enter department : ")
email = input(" Enter emailid : ")
salary = int(input(" Enter salary : "))
DOJ = input(" Enter date of joining : ")

query = f"insert into empinfo values ({empid} , '{name}' , '{dept}' , '{email}' , {salary} , '{DOJ}')"

#query = "select * from empinfo;"

cursor = connection.cursor()

cursor.execute(query)

#records = cursor.fetchall()     #   returns list of tuples

#print(records)


connection.commit()

cursor.close()

connection.close()