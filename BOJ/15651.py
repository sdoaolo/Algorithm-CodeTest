#15651_N과 M (3)

n,m = map(int, input().split())

s =[]

def go():
	if len(s) == m :
		print(' '.join(map(str,s)))
		return
	
	for i in range(1,n+1):
		s.append(i)
		go()
		s.pop()

go()