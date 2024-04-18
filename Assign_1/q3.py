#3] Write a program to accept three integer numbers and find its average.

num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))
num3 = float(input("Enter 3rd number : "))

def avg(num1,num2,num3):
    Average = float((num1 + num2 + num3) / 3 )

    print(f"Average of given numbers is : {float(Average)}")

avg(num1,num2,num3) 
