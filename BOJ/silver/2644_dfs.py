#2644_촌수계산_dfs_silver2
import sys
input = sys.stdin.readline

def dfs(v,c):
    visited[v] = True

    if v == f2:
        return c
    
    for i in graph[v]:
        if not visited[i]:
            res = dfs(i,c+1)
            if res:
                return res
    
n = int(input())
f1, f2 = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)] #누구의 부모 / 자식인지 체크
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)
res = dfs(f1, 0)

if res == None:
    print(-1)
else:
    print(res)