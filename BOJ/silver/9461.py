#9461_파도반 수열_dp_silver3
import sys
input = sys.stdin.readline

dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4,101):
    dp[i]= dp[i-2] +dp[i-3]
                
t = int(input())
for _ in range(t):
    n = int(input())#6
    print(dp[n])
