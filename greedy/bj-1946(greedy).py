import sys
N = int(sys.stdin.readline())
num = int(sys.stdin.readline())
list = [list(map,(int, sys.stdin.readline().split())) for _ in range(num)]
grid = [0]*num
list.sort(key=lambda x:x[0])
print(list)