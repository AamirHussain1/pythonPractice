def find_missing_number(arrs):
    n = len(arrs) + 1
    expected_sum = n * (n + 1) // 2

    actual_sum = 0

    for num in arrs:
        actual_sum += num

    missing_numbers = expected_sum - actual_sum

    return missing_numbers


arrays = [1, 2, 3, 4, 6, 7, 8]

print(find_missing_number(arrays))
