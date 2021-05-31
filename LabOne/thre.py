#N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket. How many apples will each single
# student get?
# How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the questions above.

n=int(input("Enter the number of students:"))
k=int(input("enter the number of apple:"))
distribute=k//n
Remaining=k%n
print(f"the remaining number of apples in basket is{Remaining}")
print(f"Number of apple each single people get is:{distribute}")
