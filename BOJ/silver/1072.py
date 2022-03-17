#1072_게임_binary search_silver3
import sys
input = sys.stdin.readline

x, y = map(int,input().split())

z = (y *100 //x)

if x == y or z ==99:
    print(-1)
    exit()

start = 1
end = x
res = 0
while start <= end:
    mid = (start+end)//2
    if (y+mid) * 100 // (x+mid) <= z:
        start = mid+1
    else:
        res = mid
        end = mid-1
        
print(res) 