n = int(input())
a = 0
b = []
while n != 0:
    t = 11 ** a
     b.append(t)
    a += 1
    n = n - 1
    print(b)
    b.remove(t)

