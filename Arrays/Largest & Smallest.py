array = [2, 53, 73, 90, 63]

largest = smallest = array[0]

for num in array:
    if num > largest:
        largest = num

    elif num < smallest:
        smallest = num

print(largest)
print(smallest)
print(max(array))
print(min(array))