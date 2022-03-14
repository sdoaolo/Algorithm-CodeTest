#2577 숫자의 개수
import sys

res = 1
for _ in range(3):
    a =  int(sys.stdin.readline().strip())
    res *= a
    
res = str(res)
for i in range(10):
    print("{}".format(res.count(str(i))))