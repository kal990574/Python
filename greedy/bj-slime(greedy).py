N=int(input())
slime=list(map(int,input().split()))
slime.sort(reverse=True)
score=0
i=0
while N>1:
    score+=slime[i]*slime[i+1]
    slime[i+1]+=slime[i]
    i+=1
    N-=1
print(score)