# Print the letter F usinf nested for loops.

lineLenght = [5, 2, 5, 2, 2]
for lenght in lineLenght:
    x_count = ''
    for count in range(lenght):
        x_count += 'x'
    print(x_count)