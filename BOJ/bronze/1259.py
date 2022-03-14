#1259_팰린드롬수

while True:
    n = input()
    if n =='0':
        exit()
    
    if n == n[::-1]:
        print('yes')
    else:
        print('no')