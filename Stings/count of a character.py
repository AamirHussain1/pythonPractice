strings = input("enter string: ")
char = input("enter character: ")
count = 0

for i in range(len(strings)):
    if strings[i] == char:
        count += 1

print(count)

