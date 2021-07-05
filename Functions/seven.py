'''''''.Q.No.7 Write a Python function that accepts a string and calculate' \
' the number of upper case letters and lower case letter'''
def UpperAndLowerCase(sentence):
 upper = 0
 lower = 0
 for i in sentence:
  if i >='A' and i <= 'Z':
     upper = upper+ 1
  elif i >= 'a' and i <= 'z':
    lower = lower + 1
    print(f"Upper case:{upper}")
    print(f"Lower case:{lower}")
UpperAndLowerCase("Heyy Ohh")