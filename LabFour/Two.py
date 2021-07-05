'''.2.Write a Python program to convert temperatures to and from celsius,
 fahrenheit.C = (5/9) * (F -32)'''
temp= float(input("Enter temperature "))
unit=input("Enter the unit of temperature(c/f) " ).lower()
if unit=='c':
    far=(9*temp/5)+32
    print ('Temperature in fahrenheit scale is ',far)
elif unit=='f':
    cel=(5/9)*(temp-32)
    print('Temperature in celsius scale is ', cel)
