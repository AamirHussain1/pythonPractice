def prime_number(number):

    # Range Method will start from 2 to that number 
    for i in range(2, number):

        # It divides that number one by one with i that is equal to numbers given by range method
        if number % i == 0:
            return f"{number} is not a Prime Number"

            # if a number exactly divides, then it breaks the loop and jump to the next iteration
            break

        else:
            return f"{number} is a Prime Number."



number = int(input("Enter Number: "))
print(prime_number(number))