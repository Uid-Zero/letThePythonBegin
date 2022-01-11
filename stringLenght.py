fullName = input("Please enter your Full Name: ")

if len(fullName) < 3:
    print ("Name must be atleast 3 charecters. ")
elif len(fullName) > 50:
    print ("Name can be length of max 50 charecters. ")
else:
    print ("Name looks Good! ")