#2667_단지번호붙이기


def dfs(x,y):
    
    
    if mapp[x][y] == 1:
        mapp[x][y] = 0
        
        
        

n = int(input())
mapp = []
for i in range(n):
	mapp.append(list(map(int,input())))
	

