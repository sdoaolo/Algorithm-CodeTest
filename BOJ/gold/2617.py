#2617_구슬 찾기_bfs_gold5
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v,graph):
    visited = [False] * (n+1)
    queue=deque()
    queue.append(v)
    visited[v] = True
    cnt = 0
    while queue:
        x = queue.popleft()
        
        for i in graph[x]:
            if not visited[i] :
                visited[i] = True
                queue.append(i)
                cnt+=1
    return cnt
            
n,m = map(int,input().split())
lightgraph = [[] for _ in range(n+1)]
heavygraph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    lightgraph[a].append(b)
    heavygraph[b].append(a)

res = 0
for i in range(1,n+1):
    lc = bfs(i,lightgraph)    
    hc = bfs(i,heavygraph)
    if lc > n//2 or hc > n//2:
        res+=1

print(res)

