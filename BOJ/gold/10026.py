#10026_적록색약
import sys
from collections import deque
#input = sys.stdin.readline

# 빨간색과 초록색의 차이를 거의 느끼지 못하는 적록색약. 
# 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역 개수를 출력

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y,S):
    queue = deque()
    queue.append([x,y])
    
    visited[x][y] = True
    
    while queue:
        r,c = queue.popleft()
        
        for i in range(4):
            rr = r+dr[i]
            cc = c+dc[i]
            
            if (0<= rr <n) and (0<=cc<n):
                if not visited[rr][cc] and graph[rr][cc] == S:
                    queue.append([rr,cc])
                    visited[rr][cc] = True

             
n = int(input())
graph = [[]*n for _ in range(n)]
for i in range(n):
    colors = input()
    for color in colors :
        graph[i].append(color)
        
visited = [[False]*n for _ in range(n)]
res = []
count = 0 


#적록색약 아님
for i in range(n):
    for k in range(n):
        if not visited[i][k]:
            bfs(i,k,graph[i][k])
            count+=1

res.append(count)

#적록색약
for i in range(n):
    for k in range(n):
        if graph[i][k] == 'G':
            graph[i][k] = 'R'

visited = [[False]*n for _ in range(n)]
count = 0 
for i in range(n):
    for k in range(n):
        if not visited[i][k]:
            bfs(i,k,graph[i][k])
            count+=1

res.append(count)


for r in res:
    print(r, end=" ")