# Operations defined as functions.

def add(digitOne, digitTwo):
    return digitOne + digitTwo

def sub(digitOne, digitTwo):
    return digitOne - digitTwo

def multiply(digitOne, digitTwo):
    return digitOne * digitTwo

def divide(digitOne, digitTwo):
    return digitOne / digitTwo

# Try-Exception to check for ValueError

try:
    digitOne = int(input("Enter your first digit: "))
    digitTwo = int(input("Enter your second digit: "))
except:
    ValueError
    print("")
    print("Ivalid!! Enter an integer instead. ")
    print("")
    quit()

operation = input("Enter your operation [ Add | Sub | Multiply | Divide ]: ").lower()

if operation == "+" or operation == "add":
    print(add(digitOne, digitTwo))
elif operation == "-" or operation == "sub":
    print(sub(digitOne, digitTwo))
elif operation == "*" or operation == "multiply":
    print(multiply(digitOne, digitTwo))
elif operation == "/" or operation == "divide":
    print(divide(digitOne, digitTwo))
else:
    print("Invalid Operation. Exiting the program. ")
