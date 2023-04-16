string = input("Enter string: ")

sorted_string_Desc = "".join(sorted(string, reverse=True))
sorted_string_Asc = "".join(sorted(string))

print(sorted_string_Asc)
print(sorted_string_Desc)