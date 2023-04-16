def find_missing_numbers(arr):

    min_num = min(arr)
    max_num = max(arr)

    all_nums = set(range(min_num, max_num+1))

    missing_numbers = all_nums - set(arr)

    return missing_numbers


array = [1, 3, 5, 6, 8, 15]
print(find_missing_numbers(array))
