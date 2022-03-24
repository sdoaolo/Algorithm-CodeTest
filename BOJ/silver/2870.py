#2870_수학숙제_string_silver4
import sys
input = sys.stdin.readline
n= int(input())
numli = ('0','1','2','3','4','5','6','7','8','9')
li = []
for i in range(n):
    s = input().rstrip()
    
    num = ""
    l = len(s)
    for k in range(l):
        if k == l-1 and s[k] in numli:
            num += s[k]
            li.append(num)
        else:
            if s[k] in numli:
                num += s[k]
            else:
                if len(num) !=0:
                    li.append(num)
                    num = ""

l = len(li)
for i in range(l):
    li[i] = int(li[i])
li.sort()
for i in li:
    print(i)