#9372_상근이의 여행_dfs_silver3

import sys
input = sys.stdin.readline

def dfs(v,cnt):
    visited[v] = True
    for i in graph[v]:
        if not visited[i] :
            cnt =dfs(i,cnt+1)
    return cnt        
    
t = int(input())

for _ in range(t):
    #국가의수, 비행기의 종류
    n, m = map(int,input().split())

    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)
    res = dfs(1,0)
    print(res)