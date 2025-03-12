a = input('Hansi usulu isteyirsiniz ? : ')
b= float(input(‘Eded 1: '))
c= float(input('Eded 2: '))

if a == '+':
    print(b + c)
elif a == '-':
    print(b - c)
elif a == '*':
    print(b * c)
elif a == '/':
    if c != 0:
        print(b / c)
    else:
        print('Sifira bolme yoxdu olmaz')