#problem is to find the k th term where n is given and order of it is in lexcigraphy order.

n = int(input("N value : "))
k = int(input("K value : "))

d = {}
li = []
for x in range(1,n+1):
    y = str(x)
    if(y[0] not in d):
        d.setdefault(y[0],[])
    d[y[0]].append(y)
for y in d:
    d[y].sort()
    li+=d[y]
print(li)
print(li[k-1])