arr = list(map(int, input().split()))
pos =[]
neg =[]
zero =[]
for i in arr:
    if i > 0:
        pos.append(i)
    if i ==0:
        zero.append(i)
    if i < 0:
        neg.append(i)
        