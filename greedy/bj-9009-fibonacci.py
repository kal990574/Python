arr =[]
j=0
result =[]
def fibo(n):
    if n in (1,2):
        return 1
    return fibo(n-1) + fibo(n-2)
for i in range(1,50):
    arr.append(fibo(i))
N=int(input())
for i in range(N):
    j = int(input())
    while(j):
        for i in range(50):
            if(fibo(i) <= j):
                m = fibo(i)
        j -= m
        result.append(m)
        result.sort()
    for i in result:
        print(i, end=' ')
