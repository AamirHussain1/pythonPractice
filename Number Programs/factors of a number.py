def factors(number):
    """
    Returns the prime factors of a positive integer n.
    """
    prime_factors = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            prime_factors.append(i)
            number //= i
        else:
            i += 1
    if number > 1:
        prime_factors.append(number)

    return prime_factors


numbers = int(input("Enter Num: "))
print(factors(numbers))
