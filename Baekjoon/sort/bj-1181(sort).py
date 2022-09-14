import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr.append(sys.stdin.readline().strip())
arr=set(arr)
arr=list(arr)
arr.sort()
arr.sort(key=lambda x: len(x))
for i in arr:
    print(i)