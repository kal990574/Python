j=0
fibo = [0,1]
for i in range(2,50):
    fibo.append(fibo[i-2] + fibo[i-1])
N=int(input())
for i in range(N):
    result =[]
    j = int(input())
    while(j):
        for i in range(50):
            if(fibo[i] <= j):
                m = fibo[i]
        j -= m
        result.append(m)
        result.sort()
    for i in result:
        print(i, end=' ')
