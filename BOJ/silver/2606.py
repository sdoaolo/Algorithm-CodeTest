#2606_바이러스
import sys
input = sys.stdin.readline

def dfs(v):
	visited[v] = True
	for i in graph[v]:
		if visited[i] == False:
			dfs(i)
	return True
					
n = int(input())
m = int(input())

graph= [[] for _ in range(n+1)]

for i in range(m):
	one, two = map(int, input().split())
	graph[one].append(two)
	graph[two].append(one)
	
visited = [False] * (n+1)

dfs(1)

print(sum(visited)-1)