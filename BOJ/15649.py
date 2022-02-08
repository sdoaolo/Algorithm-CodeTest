#15649_N과 M (1)
n,m = map(int,input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

s = []

def go():
	if len(s) == m:
		print(' '.join(map(str,s)))
		return 
	for i in range(1,n+1):
		if i not in s:
			s.append(i)
			go()
			s.pop()

go()