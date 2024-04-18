# 1] Write a Python Program find an area of a rectangle and perimeter of the rectangle.
# def fun1(length , breadth):
length = float(input("Enter number : "))
breadth = float(input("Enter number : ")) 

def fun1(length , breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print(f" area of given rectangle = {area}")
    print(f" perimeter of given rectangle = {perimeter}")


fun1(2,3)







