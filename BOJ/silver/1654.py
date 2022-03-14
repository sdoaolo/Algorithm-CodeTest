#1654_랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
li = [int(input()) for _ in range(k)]

start = 1
end = max(li)

while start <= end:
	res = 0
	mid = (start+end) // 2
	for l in li:
		res += (l//mid)
		
	if res < n:
		end = mid - 1
	else:
		start= mid + 1

print(end)