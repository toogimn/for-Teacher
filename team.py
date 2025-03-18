a = int(input("Meselelerin (problemlerin) sayin yaz: "))
s = 0
for i in range(a):
    b = input()
    c = b.split()

    d1 = int(c[0])
    d2 = int(c[1])
    d3 = int(c[2])
    if d1 + d2 + d3 >= 2:
       s=s+1
print(s)
