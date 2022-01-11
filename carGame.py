engineStatus = "stopped"

exitCar = False

while not exitCar:
    engineCommand = input("Enter an Engine Command [Help]: ").lower()
    if engineCommand == "start":
        if engineStatus != "started":
            print("Engine Started. ")
            engineStatus = "started"
        else:
            print("Engine is already started. ")
    elif engineCommand == "stop":
        if engineStatus != "stopped":
            print("Engine Stopped. ")
            engineStatus = "stopped"
        else:
            print("Engine is already stopped. ")
    elif engineCommand == "exit":
        print("Exiting the Car. ")
        exitCar = True
    elif engineCommand == "status":
        print(f"Current status of the engine: {engineStatus}")
    elif engineCommand == "help":
        print("""
        Please use below commands to use the engine:
        Start   :   To start the engine.
        Stop    :   To stop the engine.
        Exit    :   To exit the car.
        Help    :   To repeat this menu.
        Status  :   Print the current status of the engine.
        """)
    else:
        print("Invalid Command, Please use [Help] to print the valid options. ")