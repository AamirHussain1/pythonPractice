# taking number from user
number = int(input("Enter the Number: "))

# Initiliaze the sum of digits to 0
sum_of_digits = 0

# Initialize the total digit to 0, later it stores total number digits as a power(exponent)
total_digits = 0

# Assigning original number to temporary variable
temp = number

# Loop till the temp num remains greater than 0, and to get the total digits
while temp > 0:
    
    total_digits = total_digits + 1
    temp = temp // 10

# Assigning again number to temp variable, otherwise it holds the value from the above while loop
temp = number

# this loop will check number to be armstrong or not
while temp > 0:
    reminder = temp % 10
    sum_of_digits = sum_of_digits  + (reminder ** total_digits)
    temp = temp // 10

# Comparing the numbers if it matches then it is Armstrong number
if sum_of_digits == number:
    print(f"{number} is Armstrong number.")

else:
    print(f"{number} isnot Armstrong number.")

