'''game finding a secret number within 3 attempts using while loop'''
import random
number=random.randint(1,9)
print(number)
attempt=2
while attempt>=0:
    guess = int(input("Gusess the numebr from 1 to 9 : "))
    if guess == number:
        print("Your number is correct")
        break
    else:
        print(f"You have {attempt} attempt left.")
    attempt = attempt - 1