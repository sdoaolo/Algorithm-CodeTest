#1789_수들의 합_greedy_silver5
import sys
s = int(sys.stdin.readline())
hap = 0
n = 1
while hap <= s:
    hap += n
    n+=1

print(n-2) 