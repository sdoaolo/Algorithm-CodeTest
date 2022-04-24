#1343_폴리오미노_greedy_silver5

import sys
input = sys.stdin.readline

board = input().rstrip()
X_list = list(map(str,board.split('.')))

length = len(X_list)

poliomino = []
for x in X_list:
    xlen = len(x)
    if xlen == 2:
        poliomino.append('BB')
    elif xlen == 4:
        poliomino.append('AAAA')
        
    else: # 1,3,5와같이 
        if xlen%2 ==1: #홀수
            print(-1)
            exit()
        else: #6이상의 짝수
            p = ""
            # 4로 나누어떨어지면 > A만 추가 
            #아니면 몫만큼 A추가, B를 마지막에 추가
            
            aNum = xlen // 4
            p += aNum*"AAAA"
            if xlen %4 != 0:
                p += "BB"
        
            poliomino.append(p)
    
res = ""
for p in poliomino:
    if p =='':
        res+='.'
        continue
    else:
        res+=p
    res += '.'    
print(res[0:-1])