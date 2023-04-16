def palindrome(strings):
    for i in range(len(strings)):
        reversed_string = strings[::-1]

        if reversed_string == strings:
            return f"{strings} is Palindrome string"

        else:
            return f"{strings} is not a Palindrome string"


stringss = input("Enter string: ")
print(palindrome(stringss))
