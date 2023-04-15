# Function to check the number is palindrome or not
def palindrome(number):

    # Initiliaze the reverse variable to 0
    reverse = 0
    
    # Assign to number to temp variable
    temp = number

    # Loop to check the reversibility of a number
    while temp > 0:
        reminder = temp % 10
        reverse = reminder + (reverse * 10)
        temp = temp // 10

    # Comparing Original number and reversed number
    if number == reverse:
        return f"{number} is a Palindrome Number."
    
    else:
        return f"{number} is not a Palindrome Number."

number = int(input("Enter input: "))
print(palindrome(number))
