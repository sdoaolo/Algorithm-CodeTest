#1325_효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    cnt = 1
    visited = [False]*(n+1)
    visited[start] = True
    queue= deque()
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt +=1
    return cnt
                
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)
    
max = 0
res = []
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max :
        max = cnt
    res.append([i,cnt]) 

for i,cnt in res:
    if max == cnt:
        print(i, end=" ")