'''
Task -----------------condition------------------------------
Weight converter:
Input the weight of a person in either kg or lbs. If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''
weight_in_lbs=float(input("enter the weight in lbs:"))
weight_in_kg=float(input("enter the weight in kg:"))
pound=2.20462
converter=(weight_in_kg*pound)
converter2=(weight_in_lbs*pound)
if weight_in_kg==converter:
    print(converter)
elif weight_in_lbs==converter2:
    print(converter2)