import sys
a, b = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))
ab_list = a_list + b_list
result = ' '.join(map(str, sorted(ab_list)))
print(result)