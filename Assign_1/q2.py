
#2] Write a program to accept a 4 digit number and

num = int(input("Enter 4 digit number : "))

#a. Display face value of each decimal digit

def faceval(num):
    print(f"face value of given number : ")
    while(num != 0):
        temp = num % 10
        print(temp,end=" ")
        num = num // 10

faceval(num) 

#b. Display place value of each decimal digit

def placeval(num):
    count = 1000
    print(f"place value of given number : ")
    while(num != 0):
        temp = (num // count) * count
        print(temp , end=" ")
        num = num % count
        count = count // 10

placeval(num)

        
        
#c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 
#output should be
#c. 1639

def revno(num):
    print(f"place value of given number : ")
    while(num != 0):
        temp = num % 10
        print(temp , end=" ")
        num = num // 10

revno(num)

