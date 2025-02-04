no = input("Enter a number for which you want multiplication table \n")

print(f"Multiplication table of {no} is:")

for i in range(1, 11):
    print(f"{int(no)} X {i} = {int(no) * i}")
