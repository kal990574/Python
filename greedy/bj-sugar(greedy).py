N=int(input())
result=0
five=0
three=0
while True:
    if N%5==0:
        result+=(N//5)
        N=0
    else:
        N-=3
        result+=1
    if N==0:
        break
    if N<0:
        result=-1
        break
print(result)