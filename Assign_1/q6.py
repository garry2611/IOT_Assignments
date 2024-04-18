
# 6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
# epts the number as an argument.

num1 = int(input("Enter a number : "))

def fact(num1):
    fact = 1
    while num1 >= 1:
        fact = num1 * fact
        num1 = num1 - 1

    print(fact)

fact(num1)        
