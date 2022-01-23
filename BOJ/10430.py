A, B, C = map(int, input().split())
r1 = (A+B)%C
r2 = ((A%C) + (B%C))%C
r3 = (A*B)%C
r4 = ((A%C) * (B%C))%C
resStr =  '%d \n%d \n%d \n%d' %(r1,r2,r3,r4)  
print(resStr)

map(int, input().split())