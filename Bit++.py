a = int(input("Nece defe oynanilacaq?: "))
x = 0
for i in range(a):
    b = input()
    if b.count("++") > 0 :
        x = x + 1
    elif b.count("--") > 0 :
        x = x - 1
print(x)