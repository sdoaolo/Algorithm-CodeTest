#1764_듣보잡

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
d = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(m)]

db = list(set(d)&set(b))
db.sort()
l = len(db)
print(l)
for i in range(l):
    print(db[i])