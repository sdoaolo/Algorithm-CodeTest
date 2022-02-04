# 1181 단어 정렬

# 길이가 짧은 것부터
# 길이가 같으면 사전 순
import sys

n = int(input())
wordList = [sys.stdin.readline().strip() for i in range(n)]

wordL = set(wordList)
wordList = list(wordL)

n = len(wordList)
wordList.sort() # 알파벳 순 정렬 (낮은 순위 먼저 해야함)
wordList.sort(key=len) # 길이 짧은 순 (1순위는 나중에)

for i in wordList:
    print(i)
    