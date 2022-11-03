n=int(input())
t1=list(map(int,input().split()))
t1.sort()
result=0
var1=0
for i in t1:
    result+=(i*(n-var1))
    var1+=1
print(result)