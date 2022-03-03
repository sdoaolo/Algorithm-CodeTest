#7576_토마토
import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()

for i in range(n):
	for j in range(m):
		if box[i][j] == 1:
			q.append((i,j))

def bfs():
	while q:
		x,y = q.popleft()
		
		for i in range(4):
			xx = x+dx[i]
			yy = y+dy[i]
			
			# 이동하려는 좌표가 xx, yy가 box 안이며, 이동하려는 곳이 토마토(0), 아직 방문하지 않은 곳 (0) 이면 이동
			if (0<=xx<n) and (0<=yy<m) and box[xx][yy] == 0:
				# 토마토 = 1
				box[xx][yy] = box[x][y] +1
				q.append((xx,yy))
				
bfs()
res = 0
for tomatoes in box:
	if 0 in tomatoes:
		print(-1)
		exit(0)
	res = max(res, max(tomatoes))
print(res-1)