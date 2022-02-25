#10773_제로

import sys
input = sys.stdin.readline

k = int(input())

li = []

for i in range(k):
    n = int(input())
    if n!=0:
        li.append(n)
    else:
        li.pop()
    
res = 0
for i in li:
    res+= i
    
print(res)    