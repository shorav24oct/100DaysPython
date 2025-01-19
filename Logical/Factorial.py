def factorial(no):
    if no == 0 or no == 1:
        return 1
    else:
        return no * factorial(no - 1)


print(factorial(5))
