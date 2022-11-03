result=0
str=input().split('-')
for k in str[0].split('+'):
    result+=int(k)
for i in str[1:]:
    for j in i.split('+'):
        result-=int(j)
print(result)
