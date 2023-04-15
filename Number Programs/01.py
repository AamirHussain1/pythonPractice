def prime_factors(number):

    factors = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            factors.append(i)
            number = number // i

        else:
            i += 1

    if number > i:
        factors.append(number)

    return factors


num = int(input("Enter Number: "))
print(prime_factors(num))