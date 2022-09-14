import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort(key=lambda x:(x[0], x[1]))
for i in range(N):
    for j in range(2):
        print(arr[i][j], end=' ')
    print('')