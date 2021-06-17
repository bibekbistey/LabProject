#4. Given three integers, print the smallest one. (Three integers should be user input)
a=int(input("Enter first integer:"))
b=int(input("Enter second integer:"))
c=int(input("Enter third integer:"))
if a<b and a<c:
    print("a is smallest")
elif b<a and b<c:
    print("b is smallest")
elif c<a and c<b:
    print("c is smallest")
