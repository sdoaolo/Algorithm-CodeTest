#1235_학생 번호_string_silver4
import sys
input = sys.stdin.readline
n = int(input())
stdnum = []

for i in range(n):
	stdnum.append(input().rstrip())

length = len(stdnum[0])

for i in range(length-1,-1,-1):
	s = set()
	for k in range(n):
		s.add(stdnum[k][i:])
	if len(s) == n:
		s = list(s)
		print(len(s[0]))
		exit()