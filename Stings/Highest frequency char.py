def highest_frequency(strings):
    char_frequency = {}
    max_frequency = 0
    most_frequent_char = ''

    for char in strings:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    print(char_frequency)

    print(max(char_frequency))

    for char in char_frequency:
        if char_frequency[char] > max_frequency:
            max_frequency = char_frequency[char]
            most_frequent_char = char

    return most_frequent_char


string = "pineapple"
print(string)
print(f"The most frequent char in {string} is:", highest_frequency(string))
