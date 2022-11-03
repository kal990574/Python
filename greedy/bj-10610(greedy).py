import sys
N=int(sys.stdin.readline())
#0이 있는지 확인
#3*10 0이 있는지 확인후 나머지 숫자들 더했을때 3의 배수인지 확인
#맞다면 내림차순 정렬
arr=list(map(int, str(N)))
if 0 in arr and sum(arr) % 3 == 0:
    arr.sort(reverse=True)
    for i in range(len(arr)):
        print(arr[i], end='')
else:
    print("-1")
