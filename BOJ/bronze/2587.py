#2587_대표값2
import sys
data = []
sum,avg,mid = 0,0,0

for i in range(5):
	data.append(int(sys.stdin.readline()))
	sum += data[i]
	avg = sum//5

data.sort()
mid = data[2]

print(avg)
print(mid)