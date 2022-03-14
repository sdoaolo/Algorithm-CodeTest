# 2750 수 정렬하기

# n개의 수 주어졌을 때 오름차순 정렬하라
import sys

n = int(input())

li = [int(sys.stdin.readline().strip()) for i in range(n)]

tmp = 0

for i in range(0,n-1):
    for k in range(i+1,n):
        if li[i] > li[k]:
            tmp = li[k]
            li[k] = li[i]
            li[i] = tmp
            
for i in range(n):
    print(li[i])