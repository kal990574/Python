import sys
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
for i in range(len(arr)):
    print(arr[i], end=' ')