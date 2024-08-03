n = int(input())

nums = list(map(int, input().split()))
count2 = 0

for i in range(len(nums)):
    if 2 == nums[i]:
        count2 += 1
        if count2 == 3:
            idx = i+1
            break
        else:
            continue

print(idx)