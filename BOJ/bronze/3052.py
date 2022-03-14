#3052_나머지

import sys

data = set()
for i in range(10):
	data.add(int(sys.stdin.readline())%42)

print(len(data))
