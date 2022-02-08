#15650_N과 M (2)
n,m = map(int, input().split())

s = []

def go():
	l = len(s)
	if l==m:
		print(' '.join(map(str,s)))
		return

	for i in range(1, n+1):
		if i not in s:
			if l == 0 or s[l-1] < i:
				s.append(i)
				go()
				s.pop()
		
go()