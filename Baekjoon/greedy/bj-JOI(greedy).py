N=int(input())
money=1000-N
mlist=[500,100,50,10,5,1]
count=0
for i in mlist:
    if money>=i:
        count+=money//i
        money%=i
print(count)
