#8. Given a three-digit number. Find the sum of its digits.
num=int(input("Enter a three digit number:"))
a=num//100
print(a)
b=num//10%10
print(b)
c=num%10
print(c)
print(a+b+c)