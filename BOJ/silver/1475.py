#1475_방번호
import sys
input = sys.stdin.readline
n = input().rstrip()
li = [0]*10

for i in range(len(n)):
    if n[i] in ['6', '9']:
        li[6] += 1
    else:
        li[int(n[i])] += 1
        
if li[6] %2 ==0:
    li[6] = li[6] // 2
else:
    li[6] = ( li[6]//2)+1

print(max(li))    



