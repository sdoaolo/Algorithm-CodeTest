#11650 좌표 정렬하기

import sys 
n = int(input())
li = [list(map(int, input().split())) for i in range(n)]

nl = sorted(li)

for i in range(n):
    print("{} {}".format(nl[i][0],nl[i][1]))