

# 5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

sub1 = float(input(" Enter sub1 marks : "))
sub2 = float(input("Enter sub2 marks : "))
sub3 = float(input("Enter sub3 marks : "))

def avg(sub1 , sub2 , sub3 ) :
    Avg = (sub1 + sub2 + sub3) / 3
    if Avg >= 90 and Avg <= 100 :
        print(f"grade of student is : A")
    elif Avg >= 80 and Avg <= 89 :
        print(f"grade of student is : B")
    elif Avg >= 70 and Avg <= 79 :
        print(f"grade of student is : C")
    elif Avg >= 60 and Avg <= 69 :
        print(f"grade of student is : D")
    else:
        print(f"avg is below 60 and grade is : E") 

avg( sub1 , sub2 , sub3 )        
