import sys
N=int(sys.stdin.readline())
a=0
result=0
arr=list(map(int,sys.stdin.readline().split()))
for i in arr:
    cnt=0
    if i>1:
        for j in range(2,i):
            a=i%j
            if a==0:
                cnt+=1
        if cnt==0:
            result+=1
print(result)