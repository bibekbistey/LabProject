'''Q.No.8 Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
 other than 1 and itself'''
def prim(num):
 count=0
 for i in range(2,num-1):
    if num % i==0:
      count=count+1
 if count>=1:
     print('The number is not a prime no')
 else:
     print('The number is a prime number')
num=int(input('Enter a number'))
prim(num)