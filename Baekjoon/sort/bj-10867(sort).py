import sys
N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr=set(arr)
arr=list(arr)
arr.sort()
for i in range(len(arr)):
    print(arr[i], end=' ')
