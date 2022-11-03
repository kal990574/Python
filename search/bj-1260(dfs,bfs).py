from collections import deque
import sys
N, M, node = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort()
visited1 = []
visited2 = []
def bfs(graph, node, visited):
    q = deque([node])
    visited.append(node)
    while q:
        n = q.popleft()
        for i in graph[n]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return visited
def dfs(graph, node, visited):
    visited.append(node)
    for i in graph[node]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited
print(*dfs(graph, node, visited1))
print(*bfs(graph, node , visited2))
    

