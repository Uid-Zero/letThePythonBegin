# Find the largest number in a given list

list = [1, 354, 2154, 2135, 235, 324, 354, 987, 231, 0]
largestNumber = list[0]

for number in list:
    if number > largestNumber:
        largestNumber = number

print(largestNumber)