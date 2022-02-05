#1748_수 이어 쓰기1

import sys
input = sys.stdin.readline

n = int(input().strip())

start =1
ans = 0
length = 1
while start<=n:
	end = start*10-1 #
	if end > n: #356이 n일 때 end가 999가 되면 안되니까 
		end = n #end 를 n으로 설정
	ans += (end-start +1)*length
	start *= 10
	length += 1
	
print(ans)