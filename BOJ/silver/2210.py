#2210_숫자판 점프_dfs_silver2
from re import S
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c,s,sett,cnt):
    s += graph[r][c]
    if cnt ==  6:
        sett.add(s)
        return
    
    for i in range(4):
        rr = r+dr[i]
        cc = c+dc[i]
            
        if ( 0<= rr< 5) and (0 <= cc < 5) and cnt <=6:
            dfs(rr,cc,s,sett,cnt+1)

        
graph = [list(map(str,input().split())) for _ in range(5)]
            
sett = set()
    
for i in range(5):
    for k in range(5):
        dfs(i,k,"",sett,1)

print(len(sett))