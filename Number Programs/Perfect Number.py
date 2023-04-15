def is_perfect_number(number):
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number:
        return True
    else:
        return False


def perfect_numbers(start, end):
    list_of_perfect_number = []

    for number in range(start, end + 1):
        if is_perfect_number(number):
            list_of_perfect_number.append(number)

    return list_of_perfect_number


start = int(input("Enter starting point: "))
end = int(input("Enter ending point: "))
print(f"Perfect number between {start} & {end} are:", perfect_numbers(start, end))
