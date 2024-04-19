import mysql.connector

connection = mysql.connector.connect(

    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

def show():
    query = "select * from empinfo;"
    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor:
        print(row)

    cursor.close() 

def execute_query(query):

    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    cursor.close()

def add():
    empid = int(input(" Enter empid : "))
    name = input(" Enter name : ")
    dept = input(" Enter department : ")
    email = input(" Enter emailid : ")
    salary = int(input(" Enter salary : "))
    DOJ = input(" Enter date of joining : ")

    query = f"insert into empinfo values ({empid} , '{name}' , '{dept}' , '{email}' , {salary} , '{DOJ}')"

    execute_query(query)

def delete():
    empid = input("Enter empid : ")
    query = f"delete from empinfo where empid = {empid};"

    execute_query(query)

def update():
    empid = int(input(" Enter empid to be updated : "))
    dept = input(" Enter department : ")
    email = input(" Enter emailid : ")
    salary = int(input(" Enter salary : "))

    query = f"update empinfo SET dept = %s , email = %s , salary = %s where empid = %s ;"  
    val = (dept,email,salary,empid) 

    cursor = connection.cursor()
    cursor.execute(query,val)
    connection.commit()
    cursor.close()

while True:
    print("empinfo table")
    show()

    print("1. Add employee ")
    print("2. Delete employee ")
    print("3. Update employee ")
    print("4. exit ")

    choice = int(input(" Enter your choice : "))

    if choice == 1:
        add()
        show()

    elif choice == 2:
        delete()
        show()

    elif choice == 3:
        update()
        show()
    
    elif choice == 4:
        break

    else:
        print(" Invalid choice no ")

    connection.close()    
