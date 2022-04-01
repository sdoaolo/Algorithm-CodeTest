#17836_공주님을 구해라!_bfs_gold5

from collections import deque
import sys
input =sys.stdin.readline


dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):
    temp = sys.maxsize
    gram = False
    queue = deque()
    queue.append([r,c])
    visited[r][c] =1
    while queue:
        
        r,c = queue.popleft()
        
        if graph[r][c] == 2:
            temp = abs(n-1-r) +abs(m-1 -c) +visited[r][c] -1
        if r == n-1 and c == m-1: #그람과 만났을 때 temp시간으로 이동, 안만났을 땐 visited[r][c] -1 값이 이동 시간이다.  
            return min(visited[r][c] -1, temp)

    #그람 없이 이동
        for i in range(4):
            rr = r+dr[i]
            cc = c+dc[i]
   
            if (0<=rr<n) and (0<=cc<m):
                if not visited[rr][cc]:
                    if graph[rr][cc] != 1:
                        visited[rr][cc] = visited[r][c] +1
                        queue.append([rr,cc])
        
    return temp
                    
n, m , t = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]


res = bfs(0,0)

if res <= t:
    print(res)
else:
    print("Fail")