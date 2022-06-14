#2564_경비원_implements_silver1
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
storeNum = int(input())
storexy = [list(map(int,input().split())) for _ in range(storeNum)]
dx, dy = map(int,input().split())

def makexy (x,y):
    if x == 1: #북쪽
        return [0, y, x]
    elif x == 2: #남쪽
        return [m, y, x]
    elif x == 3: #서쪽
        return [y, 0, x]
    else: #동쪽
        return [y, n, x]
#1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다.
#둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리를 나타내고,
#상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리를 나타낸다.

#1 4 북쪽, 왼쪽으로부터 4칸
#3 2 서쪽, 위쪽으로부터 2칸
#2 8 남쪽, 왼쪽으로부터 8칸
#2 3 남쪽, 왼쪽으로부터 3칸
graphxy = []
for x, y in storexy:
    graphxy.append(makexy(x,y))

dx, dy, dir = makexy(dx, dy)

eastwest = [3,4]

result = 0
for x, y, d in graphxy:
    if abs(dir-d) == 1:
        if dir in eastwest:
            distance = n + min((abs(m-x)+ abs(m-dx)),(x+dx))
        else:
            distance = m + min((abs(n-y)+ abs(n-dy)),(y+dy))
    if (dir == d) or (dir in eastwest and d not in eastwest) or (d in eastwest and dir not in eastwest):  #
        distance = abs(dx - x) + abs(dy - y)


    result += distance

print(result)