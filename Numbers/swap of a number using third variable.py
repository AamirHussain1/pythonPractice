first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))

print(f"Before swapping the Value of number1 is {first_number} and number2 is {second_number}")
temp = first_number
first_number = second_number
second_number = temp

print(f"\nAfter swapping the Value of number1 is {first_number} and number2 is {second_number}")