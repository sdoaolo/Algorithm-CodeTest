#2589_보물섬_bfs_gold5
from collections import deque
import sys 
input = sys.stdin.readline

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y):
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append((x,y))
    
    visited[x][y] = 1
    max_value = 0
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            rr = r+dr[i]
            cc = c+dc[i]
            
            if (0<=rr<n) and (0<=cc<m):
                if not visited[rr][cc] and graph[rr][cc] == 'L':
                    visited[rr][cc] = visited[r][c] + 1
                    queue.append((rr,cc))    
                    max_value = max(max_value, visited[rr][cc])
        
    return max_value-1
    
n, m = map(int,input().split())
graph = [ input() for _ in range(n)]

res =0
for i in range(n):
    for k in range(m):
        if graph[i][k] == 'L':
            res = max(res, bfs(i,k))
    
print(res)