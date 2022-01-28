def check(data):
    n = len(data)
    ans = 1
    for i in range(n):
        cnt = 1
        for k in range(1,n): # start with index 1 , 두번째 칸부터 -1 부분 확인
            if data[i][k] == data[i][k-1]:
                cnt += 1
            else: 
                cnt = 1
            if ans < cnt:
                ans = cnt
        cnt = 1
        for k in range(1,n):
            if data[k][i] == data[k-1][i]:
                cnt += 1
            else: 
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans
	
n = int(input())
data = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
	for k in range(n):
		if k+1<n:
			data[i][k], data[i][k+1] = data[i][k+1], data[i][k]
			temp = check(data)
			if ans <temp:
				ans = temp
			data[i][k], data[i][k+1] = data[i][k+1], data[i][k]
		if i+1<n:
			data[i][k], data[i+1][k] = data[i+1][k], data[i][k]
			temp = check(data)
			if ans <temp:
				ans = temp
			data[i][k], data[i+1][k] = data[i+1][k], data[i][k]
print(ans)