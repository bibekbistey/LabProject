'''10. Write a Python program to convert seconds to day, hour, minutes and seconds.'''
time=int(input("enter the value of time in second :"))
day=(1/86400)*time
hour=(1/3600)*time
minutes=(1/60)*time
print(f"{time}sec is equal to {int(day)}day ,{hour} hour,{minutes} minutes")