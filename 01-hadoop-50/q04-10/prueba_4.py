with open('data.csv') as file:
    for line in file:
        line.split(' ')
        print(line[0] + ',1\n')
