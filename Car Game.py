command=""
started=False
while command.lower()!="quit":
    command=input("> ")
    if command.lower()=="start":
        if started:
            print("car is already started!")
        else:
            started=True
            print("Car started .....Ready to gear up")
    elif command.lower()=="stop":
        if not started:
            print("car is already stopped")
        else:
            started=False
            print("car stopped...")
    elif command.lower()=="help":
        print("""
          start - to start the car
          stop  - to stop the car
          quit  - to quit
          """)
    else:
        print("I dont understand that")
