'''5. A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes
, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for
the third group of 22 students. So, we need 32 desks in total.'''
no_of_students1=int(input("enter the number of students1:"))
no_of_students2=int(input("enter the number of students2:"))
no_of_students3=int(input("enter the number of students3:"))
no_of_desk1=no_of_students1//2
print(f"no of desk required in class A is:{no_of_desk1}")
no_of_desk2=no_of_students2//2
print(f"no of desk required in class B is:{no_of_desk2}")
no_of_desk3=no_of_students3//2
print(f"no of desk required in class C is:{no_of_desk3}")
rem1=no_of_students1%2
rem2=no_of_students2%2
rem3=no_of_students3%2
totaldesk=no_of_desk3+no_of_desk1+no_of_desk2+rem1+rem2+rem3
print(f"total disk required is:{totaldesk}")

