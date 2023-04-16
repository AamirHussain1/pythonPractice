# Get the integer from user
number = int(input("Enter an integer: "))

# Initiliaze the reversed number variable is 0
reversed_number = 0

# Looping till the number becomes equal to 0 i.e, when all the numbers are extracted
while number != 0:

    reversed_number = reversed_number * 10 + number % 10

    number = number // 10

print(reversed_number)
