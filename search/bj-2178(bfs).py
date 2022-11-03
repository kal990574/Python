from collections import deque
row, col = map(int, input().split())
graph = []
for i in range(row):
    graph.append(list(map(int, input())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < row and ny >= 0 and ny < col:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    return graph[row-1][col-1]
print(bfs(0,0))