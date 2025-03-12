a=input("Daxil et : ").split()
b=0
c=0
for i in range (0,len(a)):
    for t in range (i+1,len(a)):
        if a[i]>a[t]:
            b=a[i]
            c=a[t]
print(b,c)