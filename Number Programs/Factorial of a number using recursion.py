def factorial(number):
    if number == 0:
        return 1

    else:
        for i in range(1, number + 1):
            return number * factorial(number - 1)


num = 5
print(factorial(num))
