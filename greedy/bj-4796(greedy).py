import sys
arr=[]
cnt=0
result=0
while True:
    arr.append(list(map(int,sys.stdin.readline().split())))
    if arr[cnt][0]==0 and arr[cnt][1]==0 and arr[cnt][2]==0:
        break
    cnt+=1
for i in range(cnt):
    a = arr[i][2]//arr[i][1]
    b = arr[i][2]%arr[i][1]
    if arr[i][0]<b:
        b=arr[i][0]
    result=a*arr[i][0]+b
    print("Case %d: %d" %((i+1), result))