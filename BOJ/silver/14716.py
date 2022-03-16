#14716_현수막_bfs_silver1
from collections import deque
import sys
input = sys.stdin.readline

dr = [-1,1,0,0,-1,1,-1,1]
dc = [0,0,-1,1,-1,-1,1,1]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    
    while queue:
        r,c = queue.popleft()
        
        for i in range(8):
            rr = r+dr[i]
            cc = c+dc[i]
            
            if (0<=rr<m) and (0<=cc<n):
                if not visited[rr][cc] and graph[rr][cc] == 1:
                    visited[rr][cc] = True
                    queue.append((rr,cc))

m,n = map(int,input().split())
visited = [[False]*n for _ in range(m)]
graph = []
for i in range(m):
    graph.append(list(map(int,input().split())))
    
res =0 
for i in range(m):
    for k in range(n):
        if not visited[i][k] and graph[i][k] == 1:
            bfs(i,k)
            res+=1

print(res)     
