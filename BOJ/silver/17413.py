#17413_단어 뒤집기 2_string_silver3

import sys
input = sys.stdin.readline
s = input().rstrip()

flag = False
result = ""

word = ""
for i in range(len(s)):
    if flag:
        if s[i] == '>':
            flag = False
            result += ">"
        else:
            result += s[i]
            continue
    else:
        if s[i] == '<':
            flag = True

            if word != "":
                result += word[::-1]
                word = ""
            result += "<"
        else:
            if s[i] == " ":

                result += (word[::-1] +" ")
                word = ""
            else:
                word += s[i]

if result == "": #태그가 없는 것.
    word = list(map(str,word.split()))
    for w in word:
        ww = w[::-1]
        print(''.join(ww), end = " ")
else:
    if word != "":
        result += word[::-1]
    print(result)


