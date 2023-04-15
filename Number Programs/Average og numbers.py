def average(numbers):
    sum_of_numbers = 0
    average_of_numbers = len(numbers)
    for i in numbers:
        sum_of_numbers += i

    return sum_of_numbers / average_of_numbers


list = [2, 34, 33, 44, 234]
print(average(list))
