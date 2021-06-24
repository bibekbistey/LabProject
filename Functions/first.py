'''Q.No.1 Write a Python function to find the Max of three numbers'''
def max():

    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    num3=float(input("Enter third number:"))
    if num1>num2 and num1>num3:
        print("num 1 is maximum of three number")
    elif num2>num1 and num2>num3:
        print("num 2 is max of three numbers")
    else:
        print("num3 is max of three numbers")

max()
