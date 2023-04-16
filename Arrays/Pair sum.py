def pair_sum(arr, target_sum):

    pairs = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))

    return pairs


array = [2, 5, 8, 3, 9, 1, 4, 6]
target_sum = 5
print(pair_sum(array, target_sum))
