strno=0
stono=0
end=0
while end !="quit":
  inp = input('Enter an option ').lower()
  if inp == "start":
        if strno==0:
         print('car started ... ready go')
         strno=1
        elif strno==1:
         print('car has already started')
  elif inp=="stop":
       if stono==0:
           print('car stopped')
           stono=1
       elif stono==1:
           print('Car has already stopped')

  elif inp=="quit":
      end="quit"
  elif inp=="help":
      print('''
start - to start the car
stop - to stop the car
quit - to exit
''')

  else:
      print ("I can't understand this")





command = ""
started = False
#while command != "quit":
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started !!")
        else:
            started = True
            print("Car started !!...")
    elif command == "stop":
        if not started:
            print("Car is already stopped !!")
        else:
            started = False
            print("Car stopped !!..")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that !!")

