'''
Task -----------------condition------------------------------
Weight converter:
Input the weight of a person in either kg or lbs. If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''
unit = input("Enter unit (kg/lbs): ").lower()
weight = int(input("Enter your weight: "))
if unit == 'kg':
    converted_weight = weight * 2.20462
    print(f"Your weight is {converted_weight} lbs.")
elif unit == "lbs":
    converted_weight = weight * 0.453592
    print(f"Your weight is {converted_weight} kg.")
else:
    print("Use either 'kg' or 'lbs' as unit.")

