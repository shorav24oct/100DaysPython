def fibonacci(no):
    if no == 0:
        return 0
    if no == 1:
        return 1
    else:
        return fibonacci(no - 1) + fibonacci(no - 2)


print(fibonacci(6))
