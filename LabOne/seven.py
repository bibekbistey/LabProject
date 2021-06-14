'''7. You live 4 miles from university.
The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
 How long will the bus journey take? Alternatively, you could run to university.
 You jog the first mile at 7mph; then run the next two at15mph; before jogging the last at 7mph again.
 Will this be quicker or slower than the bus?'''
distance=4 #in miles
velocity_of_bus=25 #in mph
total_stops=10
time_spent_in_stop=2 #in minutes
total_time_in_stops=total_stops*time_spent_in_stop
time_taken_in_bus=(distance/velocity_of_bus)*60
total_time_by_bus=time_taken_in_bus+total_time_in_stops
print(f"the total time taken by bus is:{total_time_by_bus}")
#For jog
firstjog=(1/7)*60
secondjog=(2/15)*60
thirdjog=(1/7)*60
total_time_in_jog=firstjog+secondjog+thirdjog
print(f"the total time take to reach the uni by jogging is: {total_time_in_jog}")
if total_time_by_bus<total_time_in_jog :
    print("bus is faster")
else:
    print("jogging is faster")
