engineStatus = "stopped"
# Current status of the engine.

exitCar = False

# Sample code to test the workings of If/While loops. You can start and stop the engine or get the current status of the car. Use [Help] to take a look at the allowed commands.

def help():
    print("""
        Please use below commands to use the engine:

        Start   :   To start the engine.
        Stop    :   To stop the engine.
        Exit    :   To exit the car.
        Help    :   To repeat this menu.
        Status  :   Print the current status of the engine.
        """)

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
    else:
        help()