#2579_계단 오르기_dp_silver3_다시풀어보기
import sys
input =sys.stdin.readline

n = int(input())

li = [0 for _ in range(301)]

for i in range(1,n+1):
    li[i] = int(input())

if n == 1:
    print(li[1]) 
    exit()

dp = [0 for _ in range(301)]   
dp[1] = li[1]
dp[2] = li[1] +li[2]

for i in range(3,n+1):
    v1 = li[i] + dp[i-2]
    v2 = li[i] + li[i-1] +dp[i-3] 
    dp[i] = max(v1,v2)
    
print(dp[n])
