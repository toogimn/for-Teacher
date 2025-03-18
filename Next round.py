n= input().split()
k=input().split()
a=input().split()
s = 0
for i in range (n):
    if int(a[i]) >= int(a[k-1])  and int(a[i]) > 0:
        s = s + 1

print(s)