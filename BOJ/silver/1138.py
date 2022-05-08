#1138_한줄로 서기_implement_silver2

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))

notUse = []
for i in range(n):  
    notUse.append(i)
    
res = [0] * n
for i in range(n):
    index = notUse[li[i]]
    res[index] = str(i+1)
    notUse.remove(index)
    
print(' '.join(res))
