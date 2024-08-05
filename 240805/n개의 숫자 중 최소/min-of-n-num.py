n = int(input())

nums = list(map(int, input().split()))

min_num = nums[0]

for elem in nums:
    if min_num >= elem:
        min_num = elem

count = 0

for elem in nums:
    if min_num == elem:
        count += 1

print(min_num, count)