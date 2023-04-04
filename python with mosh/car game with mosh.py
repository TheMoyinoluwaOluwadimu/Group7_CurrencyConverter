command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is in motion!!!")
        else:
            started = True
        print("car has started")
    elif command == "stop":
        print("car has stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("syntax error")


