number = int(input("Enter a number: "))

if number > 0:
    factorial = 1
    for number in range(1, number + 1):
        factorial = factorial * (number)
    print("The factorial of", number, "is", factorial)

elif number == 0:
    print("The factorial of", number, "is 1")

else:
    print("Sorry, factorial does not exist for negative numbers")




