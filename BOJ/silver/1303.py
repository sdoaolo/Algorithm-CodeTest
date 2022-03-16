#1303_전쟁-전투_bfs_silver1from collections import deque
from collections import deque
import sys

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y,color):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    count = 0
    
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            rr = r+dr[i]
            cc = c+dc[i]
            if (0<=rr<m) and (0<=cc<n):
                if not visited[rr][cc] and graph[rr][cc] == color:
                    visited[rr][cc] = True
                    queue.append((rr,cc))
                    count+=1
    return count+1

n,m = map(int,input().split())

visited = [[False]*n for _ in range(m)]
graph = [list(input()) for _ in range(m)]

res = {"W":0,"B":0}
for i in range(m):
    for k in range(n):
        if not visited[i][k]:
            c = bfs(i,k,graph[i][k])
            res[graph[i][k]]+= c*c
        
print(res["W"], res["B"])