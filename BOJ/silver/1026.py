#1026_보물

import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
res = 0

for i in range(n):
    anum = a[i]
    bnum = b.pop(b.index(min(b)))
    res += (anum*bnum)
    
print(res)