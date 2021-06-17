#Add- no parameter no return statement
def add():
    a=int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    sum=a+b
    print(f"The sum of {a} and {b} is {sum}")
add()




#Sub- parameter and no return statement
def diff(c,d):
    difference=c-d
    print(f"The difference of {c} and {d} is {difference}")
diff(10,5)


#Mul- no-paramter and return statement
def mul():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    multiply=a*b
    print(f"The multiplication of {a} and {b} is {multiply}")
    return multiply
ans=mul()


#Div- parameter and return statement
def div(a,b):
    division=a/b
    print(f"The division of {a} and {b} is {division}")
    return division
answer=div(10,2)
