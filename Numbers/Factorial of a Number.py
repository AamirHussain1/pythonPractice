def factorial(number):
    factors = 1
    if number == 0:
        return 1

    else:
        for i in range(1, number + 1):
            factors = factors * i

    return factors


num = int(input("enter Number: "))
print(f"Factorial of a {num} is:", factorial(num))
