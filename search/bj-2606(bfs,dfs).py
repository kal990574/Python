import sys
from collections import deque
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)
cnt = 0
def dfs(graph, root, visited):
    global cnt
    visited[root] = 1
    for i in graph[root]:
        if visited[i] == False:
            dfs(graph, i, visited)
            cnt += 1
    return True
dfs(graph, 1, visited)
print(cnt)