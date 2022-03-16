#11725_트리의 부모 찾기_dfs_silver2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)
    
n = int(input())
parent = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(1,n):
    a , b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(1)

for i in range(2,n+1):
    print(parent[i])