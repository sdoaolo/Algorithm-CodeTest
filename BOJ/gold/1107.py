#미완 리모컨 미완(다시풀기)

MAX = 500000

n = int(input())
m = int(input())
if m>0:
    brk = list(map(int,input().split()))
else : brk = []

broken = [False] *10

for x in brk:
    broken[x] = True

def possible(c):
    if c == 0:
        if broken[0]: 
            return 0
        else : 
            return 1
    l = 0
    while c> 0:
        if broken[c%10]:
            return 0
        l+=1
        c //= 10
    return l

ans = abs(n-100)

for i in range(0,MAX+1):
    len = possible(i)
    if len > 0 :
        press = abs(i - n)
        if ans > len + press:
            ans = len+press
           
print(ans)