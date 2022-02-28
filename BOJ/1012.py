#1021_유기농 배추

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    queue = deque([])
    queue.append([y,x])
    
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n:
                if graph[yy][xx] == 1:
                    graph[yy][xx] = 0
                    queue.append([yy,xx])   

t = int(input())
for _ in range(t):
	
	m,n,k = map(int, input().split())
	graph = [[0]*m for _ in range(n)]

	#(x,y) = location
	for i in range(k):
		x, y = map(int, input().split())
		graph[y][x] = 1 

	res = 0

	for i in range(n):
		for k in range(m):
			if graph[i][k] == 1:
				bfs(i,k)
				res+=1
				
	print(res)