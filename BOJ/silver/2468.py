#2468_안전영역

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c,h):
	q = deque()
	q.append([r,c])
	
	while q:
		vr,vc = q.popleft()
		
		for i in range(4):
			rr = vr + dr[i]
			cc = vc + dc[i]
			
			if (0<= rr<n) and (0<=cc<n) and not visited[rr][cc] and graph[rr][cc] > h:
				visited[rr][cc] = True
				q.append([rr,cc])


n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

ans = 0

for k in range(max(map(max,graph))):
	visited = [[False]*n for _ in range(n)]
	safe = 0
	for i in range(n):
		for j in range(n):
			if graph[i][j] > k and not visited[i][j] :
				bfs(i,j,k)
				safe+=1
	ans = max(ans,safe)

print(ans)