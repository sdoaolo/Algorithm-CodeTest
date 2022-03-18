#18352_특정 거리의 도시 찾기_bfs_silver2
import sys
from collections import deque

input = sys.stdin.readline

res = []

def bfs(start):
    queue = deque()
    queue.append(start)
    cnt = 0
    visited[start] = 1

    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)

                if visited[i] == k+1:
                    res.append(i)
                    
n, m, k, x = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] *(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

bfs(x)

if len(res) == 0:
    print(-1)
else:
    res.sort()
    for i in range(len(res)):
        print(res[i])