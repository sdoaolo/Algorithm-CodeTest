#11497_통나무 건너뛰기_sort_silver1
import sys
input =sys.stdin.readline

t =  int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    li.sort()
    
    res= 0
    
    for i in range(2,n):
        res = max(res, abs(li[i] -li[i-2]))

    print(res)