#9655_돌 게임_dp_silver5

import sys
input =sys.stdin.readline

n = int(input())

d = [-1] * 1001

# 1 == 상근이  0 == 창영이
#1개 있을 땐 1번이 이김
d[1] = 1
d[2] = 0
d[3] = 1
for i in range(4,n+1):
    if d[i-1] or d[i-3] : #돌의 개수가 i개 일 때 i-1 i-3이 1이면 남은 돌의 개수는 1/3개이므로 창영이가 이긴다.
        d[i] = 0
    else:
        d[i] = 1
        
if d[n] :
    print('SK')
else:
    print('CY')