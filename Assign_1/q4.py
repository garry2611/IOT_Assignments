
#4] Write a Python function to find the maximum of three numbers.

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

def maxno(num1,num2,num3):
    if num1 > num2  and num1 > num3 :
        print(f"num1 = {num1} is maximum number")
    elif num2 > num3  and num2 > num3 :
        print(f"num2 = {num2} is maximum number")   
    elif num3 > num1  and num3 > num2:
        print(f"num3 = {num3} is maximum number")
    else:
        print(f"all no's are equal")    
    
maxno(num1,num2,num3)    
        