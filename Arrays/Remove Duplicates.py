import array
arr, count = [], []
size = int(input("Enter size of array: "))

for elements in range(size):
    count.append(0)
    elements = input("Enter the elements of array: ")
    arr.append(elements)

for x in range(size):
    count[arr[x]] = count[arr[x]] + 1
    if count[arr[x]] == 1:
        print(arr[x])
