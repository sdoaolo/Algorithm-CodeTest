#15903_카드 합체 놀이_greedy_sllver2

import sys
input = sys.stdin.readline

n , m = map(int,input().split())
cards = list(map(int,input().split()))

cards.sort()
for i in range(m):
    sum = cards[0] + cards[1]
    cards[0], cards[1] = sum, sum
    cards.sort()
    
res = 0
for card in cards:
    res += card

print(res)