#2644_촌수계산
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
	q = deque()
	q.append(start)
	
	while q:
		v = q.popleft()
		
		for i in graph[v]:
			if visited[i]== False:
				visited[i] = visited[v]+1 #@@@
				q.append(i)
		
n = int(input())
one, two = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] *(n+1)
for i in range(m):
	a,b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

bfs(one)

print(visited[two] if visited[two] > 0 else -1) #@@@@@