def remove_duplicates(strings):
    string_without_repeated_char = ""

    for char in strings:
        if char not in string_without_repeated_char:
            string_without_repeated_char += char

    return string_without_repeated_char


string = "ppyyythhooonnn"
print(remove_duplicates(string))
