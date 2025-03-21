x = 10


def my_function():
    global x
    x = 15
    y = 5
    print(f"local value of Y is {y}")


print(f"global value of X is {x}")
my_function()
print(f"global value of X is {x}")