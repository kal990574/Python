from collections import deque
import sys
case = int(sys.stdin.readline())
cnt = [0] * case
for box in range(case):
    M, N, K = map(int, sys.stdin.readline().split())
    b_list = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    graph = [[0]*M for _ in range(N)]
    for a,b in b_list:
        graph[b][a] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < N and ny >= 0 and ny < M:
                    if graph[nx][ny] == 1:
                            graph[nx][ny] = 0
                            q.append((nx, ny))
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt[box] += 1
for i in range(case):
    print(cnt[i])