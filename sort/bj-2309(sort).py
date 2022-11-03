import sys
arr=[]
all = 0
for i in range(9):
    arr.append(int(sys.stdin.readline()))
    all+=arr[i]
lie = all-100
for i in range(0,9):
    for j in range(i+1,9):
        if arr[i]+arr[j]==lie:
            a=arr[i]
            b=arr[j]
            break
arr.remove(a)
arr.remove(b)
arr.sort()
for i in arr:
    print(i)
            

"""
9명의 난쟁이
7명이 진짜
7명 더하면 100
9명에서 가짜 2명 빼면 100
다 더해서 
"""