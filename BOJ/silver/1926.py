#1926_그림_bfs_silver1
import sys
from collections import deque 
input = sys.stdin.readline

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    count = 0
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            rr = r+dr[i]
            cc = c+dc[i]
            
            if (0<=rr<n) and (0<=cc<m):
                if not visited[rr][cc] and graph[rr][cc] ==1:
                    visited[rr][cc] = True
                    queue.append((rr,cc))
                    count+=1
    return count 
                  
n,m = map(int,input().split())

visited= [[False]*m for _ in range(n)]
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    
res = []
for i in range(n):
    for k in range(m):
        if not visited[i][k] and graph[i][k] == 1:
            c = bfs(i,k)
            if c == 0:
                c+=1
            res.append(c)

if len(res) == 0:
    print(len(res))
    print(0)
else:
    print(len(res))
    print(max(res))