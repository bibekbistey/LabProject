#10. Write a Python program to sum of three given integers. However, if two values are equal sum will
# be zero.
a=int(input("Enter first integer:"))
b=int(input("Enter second integer:"))
c=int(input("Enter third integer:"))
sum=a+b+c
if a==b or b==c or a==c:
    sum1=0
    print(f"The sum between three number is {sum1}")
else:
    print(sum)