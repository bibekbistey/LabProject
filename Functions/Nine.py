'''.Q.No.9 Write a Python function that checks whether a passed string is palindrome or not
.Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
'''''' e.g., madam or nurses run.'''


def Palindrome():
    a=(input("Enter a string:"))
    b=a[::-1]
    if a==b:
        print("IT is a palindrome")
    else:
        print("It is not a palindrome")
Palindrome()