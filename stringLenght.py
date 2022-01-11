fullName = input("Please enter your Full Name: ")

# Enter your name and this program will fail if the length is less than 3 char, or greated than 50 char.

if len(fullName) < 3:
    print ("Name must be atleast 3 charecters. ")
elif len(fullName) > 50:
    print ("Name can be length of max 50 charecters. ")
else:
    print ("Name looks Good! ")