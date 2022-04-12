#13699_점화식_dp_silver4

import sys
input = sys.stdin.readline

n = int(input())

d = [-1] * 36

d[0] = 1

for i in range(1,n+1):
    hap = 0
    for k in range(0,i):
        hap += (d[k]* d[i-k-1])
    
    d[i] = hap

print(d[n])