#1449_수리공 항승_greedy_silver3
import sys
input = sys.stdin.readline

n,l = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
tape,res  = 0,0 

for i in li :
    if tape < i:
        tape = i-0.5+l
        res+=1
    else:
        continue
    
print(res)