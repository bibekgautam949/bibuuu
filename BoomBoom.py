for numbers in range(1,100):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print('Boom Boom ',numbers)
    elif numbers % 3 == 0:
        print('Boom ',numbers)
    elif numbers % 5 == 0:
        print('Nepse ',numbers)
    else:
        print('Doom ',numbers)

print('Finally, Boom Boom')