n = int(input())
nums = list(map(int, input().split()))

max = 2
min = 1000000

for i in range(n):
    if min > nums[i]:
        min = nums[i]
    if max < nums[i]:
        max = nums[i]

print(min*max)