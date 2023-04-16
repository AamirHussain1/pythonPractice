def remove_char(string):
    char = input("char: ")
    for i in string:
        if i == char:
            return string.replace(i, "")


strings = input("Enter String: ")
print(remove_char(strings))
