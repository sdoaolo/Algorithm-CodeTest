#16395_파스칼의 삼각형_dp_silver5

import sys
input = sys.stdin.readline

n,k = map(int,input().split())

graph = [[] for _ in range(n)]
graph[0].append(1)

for i in range(1,n):
    graph[i] = list([-1] for _ in range(i+1))
    for j in range(i+1):
        if j == 0 or j == i:
            graph[i][j] = 1
        else:
            graph[i][j] = graph[i-1][j]+graph[i-1][j-1]
     

print(graph[n-1][k-1])