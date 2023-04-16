def sum_of_digits(number):
    if number == 0:
        return 0

    else:
        return number % 10 + sum_of_digits(number // 10)


number = int(input("Enter Number: "))
print(f"The sum of all digits of {number} is:", sum_of_digits(number))
