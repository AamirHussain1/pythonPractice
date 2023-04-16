def fibonacci(limit):

    # In fibonacci series first two numbers are fixed i.e, 0 & 1
    first_number = 0
    second_number = 1 

    if limit == 0:
        return 0

    elif limit == 1:
        return 1

    else:
        return fibonacci(limit-1) + fibonacci(limit-2)


number = int(input("Enter the Number: "))
for i in range(0, number):
    print(fibonacci(i), end=" ")