'''6. Solve each of the following problems using Python Scripts.
Make sure you use appropriate variable names and comments.
 When there is a final answer have Python print it to the screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.'''
mass=float(input("enter the weight of a person in kg:"))
height=float(input("enter the height of a person in m:"))
BMI=mass/(height**2) #formula of BMI is mass/(height)^2
print(f"the body mass index is {BMI}")
