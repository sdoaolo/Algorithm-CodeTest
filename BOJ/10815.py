# 10815_숫자 카드 
import sys
input = sys.stdin.readline

def binary_check(arr, target, start,end):
	while start <=end:
		mid = (start+end)//2
		
		if target == arr[mid] :
			return mid
		elif arr[mid] > target:
			end = mid-1
		else:
			start = mid+1
	return None
	
n = int(input())
li = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

li.sort()
#print(li) 
#[-10, 2, 3, 6, 10]

for x in check:
	res = binary_check(li, x, 0, n-1)
	if res is not None:
		print("1", end=" ")
	else:
		print("0", end=" ")