#20365_블로그2_string_silver2
import sys
input = sys.stdin.readline

n = int(input())
colors = input().rstrip()

colorCount = {'R':0, 'B':0}
colorCount[colors[0]] = 1

for i in range(1,n):
    if colors[i] != colors[i-1]:
        colorCount[colors[i]] += 1

res = 1 + min(colorCount.values())
print(res)
