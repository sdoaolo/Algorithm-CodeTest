#1245_농장 관리_bfs/dfs_gold5_나중에 다시보기

import sys
input = sys.stdin.readline

def dfs(r,c):
    global ispeak
    visited[r][c] = True
    
    for i in range(8):
        rr = r + d[i][0]
        cc = c + d[i][1]

        if (0<=rr<n) and (0<=cc<m):
            if graph[rr][cc] > graph[r][c]: 
                ispeak = False
            if not visited[rr][cc] and graph[rr][cc] == graph[r][c]:
                dfs(rr,cc)
    
n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*(m) for _ in range(n)]
d = [(-1,1),(-1,-1),(1,1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)]

cnt =0 
for i in range(n):
    for k in range(m):
        if not visited[i][k] and graph[i][k] > 0:
            ispeak = True
            dfs(i,k)
            if ispeak:
                cnt +=1
                 
print(cnt)