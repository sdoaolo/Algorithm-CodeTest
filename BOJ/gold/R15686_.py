#15686_치킨배달_구현/브루트포스_gold5
#from itertools imoprt combinations
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int,input().split())

city = []
house = []
chicken = []

#data입력 및
#치킨집의 rc 정보와 
#그냥 집의 rc 정보를 담은 변수 제작
for r in range(n):
    row = list(map(int,input().split()))
    city.append(row)
    for c in range(n):
        if row[c] == 1:
            house.append([r,c])
        elif row[c] == 2:
            chicken.append([r,c])

minVal = sys.maxsize
chicken__ = combinations(chicken, m)

# combination으로 조합 만들어서 최소의 경우로만 테스트
for ch in chicken__: #ch에는 r,c 리스트가 들어있음. >>  m개
    chickenStreet = 0
    for home in house: # 각 집별로 m개의 치킨거리를 다 더한 값이 최소인 경우를 찾아야함. 
        chickenStreet += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch]) #i[0] == r i[1] == c # m개의 치킨집과 거리 비교, 가장 작은 치킨거리 구함. 
        if minVal <= chickenStreet: break 
    if chickenStreet < minVal: minVal = chickenStreet

print(minVal)