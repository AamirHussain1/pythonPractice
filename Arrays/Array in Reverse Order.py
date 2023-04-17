import array

size_of_array = int(input("Enter the Size of array: "))

arr = []



for i in range(0, size_of_array):
    element = int(input("Enter the Elements of Array: "))
    arr.append(element)

for i in range(size_of_array-1, -1, -1):     
    print(arr[i], end=" ")

