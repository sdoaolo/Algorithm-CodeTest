#1501_영어 읽기_String_gold5

import sys
input = sys.stdin.readline

n = int(input())
dictionary = [input().rstrip() for _ in range(n)]
m = int(input())
strings = [input().rstrip() for _ in range(m)]

#문자열에서 각 문자들이 몇개씩 있는지 체크후 딕셔너리로 반환

def countChar2(s):
    slength = len(s)
    d = {}
    s = sorted(s)
    for i in range(slength):
        if s[i] in d:
            d[s[i]] +=1
        else:
            d[s[i]] = 1

    return d

#사전에 정의된 문자열들의 각 문자 개수 세어서 딕셔너리 생성 및 리스트에 append
countdict = []
for s in dictionary:
    d = countChar2(s)    
    countdict.append(d)
    
#각 문장
for string in strings:
    #문장에 단어가 여러개일 수 있으므로 나눠서 리스트에 넣어줌
    stringlist = list(map(str,string.split()))
    countBool = False
    #문장 해석하는 경우의 수이므로 단어의 해석 경우를 찾고 곱해주어야 해서 res = 1
    res = 1
    for s in stringlist: #단어별로 해석 가능한 개수 체크
        cnt = 0
        #단어가 2보다 작으면 앞뒤 자른거 비교가 의미가 없다.
        if len(s) <=2:
            for dict in dictionary:
                if s == dict:    
                    cnt+=1
        else:                    
            d = countChar2(s) 
            for i in range(len(countdict)): #사전에서 개수 센거 하나씩 가져와서
                if countdict[i] == d: #지금 단어와 개수 비교후 같으면
                    if dictionary[i][0] == s[0] and dictionary[i][-1] == s[-1]: #사전과 맨앞뒤가 같은지 체크
                        cnt+=1 #개수 1 증가
                        
        if cnt != 0:
            res*=cnt
            countBool = True
             
    if countBool == False : #한단어라도 사전에 없으면 False이기 떄문에 이럴경우 res = 0 처리
        res = 0
                    
    print(res)
    