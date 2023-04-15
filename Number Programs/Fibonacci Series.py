def fibonacci(limit):

    # In fibonacci series first two numbers are fixed i.e, 0 & 1
    first_number = 0
    second_number = 1
     

    if limit == 0:
        print(first_number)

    else:
        print(first_number, second_number, end=" ")

        for i in range(2, limit):

            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number

            print(next_number)

number = int(input("Enter the Number: "))
fibonacci(number)