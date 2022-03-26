#9625_BABBA_dp_silver5_다시 풀어보기!
import sys
input = sys.stdin.readline
k = int(input())

a = [1]
b = [0]

#i는 0부터 시작하므로 0번째 인덱스의 개수부터 k-1까지 해주면 됨.
for i in range(k):
    a.append(b[i])
    b.append(b[i]+a[i])

print(f'{a[-1]} {b[-1]}')


# a > b > ba > bab > babba > ...
# a의 개수는 이전 b의 개수와 같다
# b의 개수는 이전 b의 개수와 a의 개수를 더한 값과 같다. 

