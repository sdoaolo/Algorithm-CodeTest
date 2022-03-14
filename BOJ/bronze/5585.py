#5585_거스름돈

import sys
input = sys.stdin.readline

a = int(input())
last = [500,100,50,10,5,1]
n = 1000-a
res = 0

for l in last:
	if l <= n:
		use= n//l
		res += use
		n = n - (use * l)

print(res)