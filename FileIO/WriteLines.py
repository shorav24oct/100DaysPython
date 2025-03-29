file = open('input2.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    file.writelines(line + '\n')

file.close()
