N=int(input())
arr=[]
count=0
key=0
for _ in range(N):    
    first,second=map(int,input().split())
    arr.append([first,second])
arr.sort(key=lambda x:(x[1],x[0]))
for a,b in arr:
    if key<=a:
        count+=1
        key=b
print(count)
