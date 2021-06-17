'''WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –> first,
 more than 40% –> pass, less than 40% –> fail'''
a=int(input("enter the marks of first subject:"))
b=int(input("enter the marks of second subject:"))
c=int(input("enter the marks of third subject:"))
d=int(input("enter the marks of fourth subject:"))
total_marks=a+b+c+d
print(total_marks)
percentage=(total_marks)/400*100
print(percentage)
if percentage>=70:
    print("You got distinction")
elif percentage>60 and percentage<70:
    print("You got first division")
elif percentage>40 and percentage<60:
    print("You are pass")
else:
    print("you are fail")