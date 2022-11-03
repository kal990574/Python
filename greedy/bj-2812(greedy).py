n, k = input().split()
n, k = int(n), int(k)
###again
num = input()
ans = []
del_cnt = k
for i in range(n):
    while len(ans) > 0 and del_cnt > 0:
        if int(ans[-1]) < int(num[i]):
            ans.pop()
            del_cnt -= 1
        else:
            break
    ans.append(num[i])

ans = ''.join(ans)
print(ans[:n-k])