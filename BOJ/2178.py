#2178_미로 탐색

from collections import deque 

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue:
           x, y = queue.popleft()
           
           for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
           
                if xx < 0 or xx >= n or yy < 0 or yy >=m:
                    continue
                if graph[xx][yy] == 0:
                    continue
           
                if graph[xx][yy] == 1:
                    graph[xx][yy] = graph[x][y] +1
                    queue.append((xx,yy))      
    return graph[n-1][m-1]
               

n, m = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []

for _ in range(n):
    li = list(map(int, input()))
    graph.append(li)
    
print(bfs(0,0))