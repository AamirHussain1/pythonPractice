def find_duplicates(arr):
    frequency = {}

    for nums in arr:
        if nums in frequency:
            frequency[nums] += 1

        else:
            frequency[nums] = 1

    duplicates = []

    for nums, count in frequency.items():
        if count > 1:
            duplicates.append(nums)

    return duplicates


array = [1, 1, 5, 7, 88, 99, 4, 66, 8, 5, 88, 99, 4]
print(find_duplicates(array))