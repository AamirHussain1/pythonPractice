number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

print(f"Before swapping the Value of number1 is {number1} and number2 is {number2}")

# By using the tuple pickling & unpickling, we can swap the two numbers without using third variable
number1, number2 = number2, number1

print(f"\nAfter swapping the Value of number1 is {number1} and number2 is {number2}")