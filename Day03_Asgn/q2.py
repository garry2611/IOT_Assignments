#* Write a python program to print all employees, employees of given department, 
# employee with highest and lowest salary
import mysql.connector

connection = mysql.connector.connect(

    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

def show():

    query = "select * from empinfo ;"
    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor:
        print(row)
    cursor.close()

def show_dept():

    query = "select * from empinfo where dept = %s ;"
    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor:
        print(row)
    cursor.close()

def highest_salary():

    query = "select * from empinfo where order by sal desc;"
    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor:
        print(row)

    cursor.close()

def lowest_salary():
    query = "select * from empinfo where order by sal asc;"
    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor:
        print(row)

    cursor.close()

while True:

    choice = int(input("Enter 1 to show all dept , Enter 2 to show employees of given dept , Enter 3 to show employees with highest salary order , Enter 4 to show employees with lowest salary"))

    match choice:
        case 1:
            print("showing all employees")
            show()

        case 2:
            dept = input("Enter name of dept : ")
            print(f"showing employees of given dept : '{dept}'")
            show_dept()

        case 3:
            print("showing employees with highest salary  ")
            highest_salary()

        case 4:
            print("showing employee with lowest salary")
            lowest_salary()

        case 5:
            print("invalid choice")

    connection.close()                            

