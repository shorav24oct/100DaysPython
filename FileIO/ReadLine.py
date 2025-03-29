file = open('marks.txt', 'r')
i = 0
while True:
    i = i + 1
    line = file.readline()
    if not line:
        break

    marks1 = line.split(',')[0]
    marks2 = line.split(',')[1]
    marks3 = line.split(',')[2]

    print(f"Marks of student {i} in Maths is: {marks1}")
    print(f"Marks of student {i} in English is: {marks2}")
    print(f"Marks of student {i} in SST is: {marks3}")

file.close()
