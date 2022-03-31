#18310_안테나_sort_silver3

import sys
input = sys.stdin.readline

n = int(input())

li = list(map(int,input().split()))

li.sort()
print(li[(n-1)//2])
