#1459_걷기

x,y,w,s = map(int,input().split())
# 현재 0,0에 있고, 
# x, y까지 가는데 
# 한블록 이동시 (x+1)or y+1 w시간이 걸리고
# 대각선 한블록 이동시 S만큼 걸린다

# 그리디를 사용해야하므로

#1번 x > y로만 이동하는 경우
#대각선으로 쭉 가다가 마지막에 x y로 이동하는 경우
#