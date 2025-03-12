a = input('Enter word: ')
if len(a) > 10:
    print(f'{a[0]}{len(a)-2}{a[len(a)-1]}')
else:
    print(a)