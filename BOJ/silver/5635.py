#5635_생일_implement,sort_silver5
import sys
input = sys.stdin.readline
n = int(input())
li = []

for i in range(n):
    name, d, m, y = map(str,input().split())
    
    if len(m) == 1:
        m = "0"+m 
    bday = y+m+d 
    
    li.append([name,bday])
        
li.sort(key = lambda x :x[1])

print(li[-1][0])
print(li[0][0])
