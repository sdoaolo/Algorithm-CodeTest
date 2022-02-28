#11724_연결 요소의 개수
import sys
input = sys.stdin.readline

def dfs(v):
	visited[v] = True
	
	for i in graph[v]:
		if visited[i] == False:
			dfs(i)
			
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

visited = [False] *(n+1)

for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

for i in range(n+1):
	graph[i].sort()
	
res = 0

for i in range(1, n+1):
	if visited[i] == False:
		dfs(i)
		res +=1
		
print(res)