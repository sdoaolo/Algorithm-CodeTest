#7568_덩치

import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

res = []
count = 0

for i in range(n):
    one = li[i]
    count = 0
    for k in range(n):
        if i==k:
            continue
        two = li[k]
        if one[0] <two[0] and one[1] <two[1]:
            count+=1
        
    print(count+1, end=" ")