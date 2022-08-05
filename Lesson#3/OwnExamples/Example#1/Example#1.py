print ("""\nHello.\n
By using this little program you are going to able to determine
what is the largest divisor of the input number and whether or not your number is even or odd. The divisors will only
be the numbers from 2 to 10.
Enjoy :)\n""")

print("Input a number:")
number = int(input())

again = 1
while again == 1:
    if number % 10 == 0:
        print("This number is multiple of 10 and is even")
    elif number % 9 == 0 and number % 2 == 0:
        print("This number is multiple of 9 and is even")
    elif number % 9 == 0 and number % 2:
        print("This number is multiple of 9 and is odd")
    elif number % 8 == 0:
        print("This number is multiple of 8 and is even")
    elif number % 7 == 0 and number % 2 == 0:
        print("This number is multiple of 7 and is even")
    elif number % 7 == 0 and number % 2:
        print("This number is multiple of 7 and is odd")
    elif number % 6 == 0:
        print("This number is multiple of 6 and is even")
    elif number % 5 == 0 and number % 2 == 0:
        print("This number is multiple of 5 and is even")
    elif number % 5 == 0 and number % 2:
        print("This number is multiple of 5 and is odd")
    elif number % 4 == 0:
        print("This number is multiple of 4")
    elif number % 3 == 0 and number % 2 == 0:
        print("This number is multiple of 3 and is even")
    elif number % 3 == 0 and number % 2:
        print("This number is multiple of 3 and is odd")
    elif number % 2 == 0:
        print("This number is multiple of 2 and is even")
    else:
        print("This number's largest divisor is the number itself. Also, your number is odd")

    print('\nDo you want to input another number?(1 - yes; other number means "no")')
    again = int(input())
    if again == 1:
        print("Input a number:")
        number = int(input())
        number = abs(number)
    else:
        print("\nThank you for using this software ;)")