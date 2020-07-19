def collatz(number):

    try:
        if number == 1:
            print("Collatz Complete.")
        elif number % 2 == 0:
            print(int(number // 2))
            collatz(number / 2)
        else:
            print(int(3 * number + 1))
            collatz(number * 3 + 1)

    except ValueError:
        print("""The information you entered is NOT an integer. 
                Definition: a whole number; a number that is not a fraction.""")

print('Enter a number: ')
number = int(input())

collatz(number)

