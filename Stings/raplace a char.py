strings = input("Enter string:")

char = input("Enter char: ")

if strings.isspace():
    new_string = strings.replace(char, " ")
    print(new_string)

else:
    print("No space is there..")
