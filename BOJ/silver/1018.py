#1018_체스판 다시 칠하기_brute force_silver5_이게실버5..?
#다시 풀어보기 ㅠ
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board =[]
for i in range(n):
    board.append(list(map(str,input().rstrip())))

count = []
#체스판 8*8 제작 2중 for 
#n , m 이 8이면 한번만 작동하면 되므로 n-7. m-7 로설정하면 됨
for a in range(n-7):
    for b in range(m-7):
        bi = 0 #BWBW 순서
        wi = 0 #WBWB 순서 
        
        # (8*8) 체스판 돌기
        for i in range(a,a+8):
            for k in range(b,b+8):
                if (i+k)%2 == 0: #board의 가장 첫번째 색깔 모임
                    if board[i][k] != 'W': #'w'인지 체크해서 w 아닌거 있으면 
                        wi+=1 #w first index 증가
                    if board[i][k] != 'B': # 'b'가 맨처음이면 b 아닌거 체크해서 bi index증가
                        bi+=1                        
                else: #board의 두번째 색깔 모임
                    if board[i][k] != 'B':  #wi는 w가 처음이므로 여기서 체크하는건 이 구간이 b 인지임
                        wi+=1
                    if board[i][k] != 'W': # 얘도 마찬가지 bi는 b가 처음 w가 다음인데 아닌거 있으면 개수 세려고 bi
                        bi+=1    
        count.append(wi)
        count.append(bi) #둘다 떄려 넣고 
                 
print(min(count)) #가장 작은거 출력