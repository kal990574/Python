import sys
from collections import deque
N = int(sys.stdin.readline())
graph =[]
for _ in range(N):
    graph.append(list(map(int, input())))
map = [[0]*N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
result = []
box = 0
def bfs(x,y):
    global box
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    box = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    box += 1
    return
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i,j)
            result.append(box)
            box = 0
            cnt += 1
print(cnt)
result.sort()
for i in range(cnt):
    print(result[i])