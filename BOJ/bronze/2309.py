# 일곱난쟁이
s= []
sum = 0
for i in range(9):
	a = int(input())
	s.append(a)
	sum += a

n1 = 0
n2 = 0

for i in range(8):
	for j in range(i+1,9):
		if sum - s[i]-s[j] == 100:
			n1 = s[i]
			n2 = s[j]

s.remove(n1)
s.remove(n2)
s.sort()

for v in s:
	print(v)