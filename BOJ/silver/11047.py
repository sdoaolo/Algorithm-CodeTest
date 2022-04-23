#11047_동전 0_greedy_silver3

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
    
last = k

coins.sort(reverse=True)

cnt = 0
for coin in coins:
    if last <= 0:
        break
    if coin <= last:
        cnt += (last//coin)
        last %= coin
        
print(cnt)    