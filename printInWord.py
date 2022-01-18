# Print your Phone Number in words using dictioneries.

convertWord = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

phoneNumber = input("Please enter your Phone Number: ")
numberInWord = ""

for numberIndex in phoneNumber:
    numberInWord += convertWord.get(numberIndex, "!") + " "

print(numberInWord)
print(f"Your Phone Number: {phoneNumber}")