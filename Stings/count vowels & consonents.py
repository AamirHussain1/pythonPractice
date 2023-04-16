strings = input("Enter string: ")
vowels = ["a", "e", "i", "o", "u"]

vowels_count = 0
consonent_count = 0

for i in strings:
    if i in vowels:
        vowels_count += 1

    else:
        consonent_count += 1


print(f"The total number of vowels in {strings} is: ", vowels_count)


print(f"The total number of consonents in {strings} is: ", consonent_count)
