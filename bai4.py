a,b,c,d=map(int,input().split())
min=a
if min>b:
    min=b
if min>c:
    min=c
if min>d:
    min=d
max=a
if max<b:
    max=b
if max<c:
    max=c
if max<d:
    max=d
print(min,max)