n = int(input())

nums = list(map(int, input().split()))

m1 = m2 = nums[0]

for i in range(len(nums)):
    if m1 <= nums[i]:
        m1 = nums[i]

nums.remove(m1)
#최댓값을 가지는 원소 제거

for j in range(len(nums)):
    if m2 <= nums[j]:
        m2 = nums[j]

print(m1, m2)