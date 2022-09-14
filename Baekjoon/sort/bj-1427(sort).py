import array
import sys
N=sys.stdin.readline()
arr=list(N)
arr.sort(reverse=True)
N="".join(arr)
print(N)