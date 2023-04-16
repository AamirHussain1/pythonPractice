def second_largest(arr):
    largest = arr[0]
    second_largest = arr[0]

    for nums in range(len(arr)):
        if arr[nums] > largest:
            largest = arr[nums]

    for nums in range(len(arr)):
        if arr[nums] > second_largest and arr[nums] != largest:
            second_largest = arr[nums]

    return second_largest

array = [22, 56, 89, 55, 809, 90]
print(second_largest(array))
