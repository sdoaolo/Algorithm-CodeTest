#1920_수 찾기

import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
	while start <=end:
		mid = (start+end)//2
		
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			end = mid-1
		else:
			start = mid +1
	return None		
	
n = int(input())

li = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

li.sort()

for x in check:
	res = binary_search(li,x, 0,n-1) 
	if res is not None:
		print(1)
	else:
		print(0)