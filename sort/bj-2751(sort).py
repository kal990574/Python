import sys
#에라토스테네스의 체
a = int(sys.stdin.readline())
arr=[]
for i in range(a):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in arr:
    print(i)