#4963_섬의 개수
from collections import deque
import sys
input = sys.stdin.readline

dr = [-1,1,0,0,1,-1,1,-1]
dc = [0,0,-1,1,-1,-1,1,1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    
    while queue:
        r,c = queue.popleft()
        
        for i in range(8):
            rr = r+dr[i]
            cc = c+dc[i]
            if (0 <= rr <h) and (0<=cc<w):
                if graph[rr][cc] == 1 and not visited[rr][cc]:
                  queue.append([rr,cc])
                  visited[rr][cc] = True
                  
        
while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0 :
        break

    graph = [list(map(int,input().split())) for i in range(h)]
    visited = [[False]*w for _ in range(h)]
    res = 0
    for i in range(h):
        for k in range(w):
            if graph[i][k] == 1 and not visited[i][k]:
                bfs(i,k)
                res+=1
                
    print(res)