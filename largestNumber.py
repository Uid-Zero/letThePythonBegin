# Find the largest number in a given list

try: 
# Ask user for input
    user_input = input("Enter numbers separated by commas: ")

    # Convert input string into a list of integers
    list = [int(x.strip()) for x in user_input.split(',')]

    if len(list) == 0:
        print("The list is empty. ")
    else:
        largestNumber = list[0]
        for number in list:
            if number > largestNumber:
                largestNumber = number
        print(largestNumber)

except ValueError:
    print("Please only enter valid int values.")