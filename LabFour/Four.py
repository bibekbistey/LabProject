'''4.
Write a Python program to construct the following pattern, using a nested for loop.
    * * ** * * * * * * * * * * * * * * * * * * * * *'''
for i in range(0,10):
    if i<=5:
        i=i+1
    print(i*"*")
    for j in range(0,6):
        if j>=5:
            j=j-1
    print(j * "*")

