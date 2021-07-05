'''3.Write a Python program to guess a number between 1 to 9.Note :User is prompted to enter a guess.
 If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess,
  user will get a "Well guessed!" message, and the program will exit.'''
import random
random=random.randint(1,9)
print(random)
for i in range(1,10):
    a=int(input("Enter a random number between 1 to 9:"))
    if a!=random:
        i=i+1
    elif a==random:
         print("Well Guessed")
         break
