#숫자가 공백을 사이에 두고 주어지는 이상, -999 or 999가 주어지는 그 순간 입력을 끊는 건 불가.
#(지금의 내 실력으로는 불가)
#일단 주어지는 숫자는 다 받고, 그 뒤에 배열을 자른다.

nums = list(map(int, input().split()))

nums_max = nums[0]
nums_min = nums[0]

for i in range(len(nums)):
    if nums[i] != -999 or 999:
        continue
        #왜 코드를 if nums[i] == 999 or 999: break로 짜면 작동이 안 되는 거지? break 문을 바로 넣으면 안 되나?
    else:
        break

nums_mod = nums[:i]
#999 or -999 제외

for elem in nums_mod:
    if nums_max <= elem:
        nums_max = elem

    if nums_min >= elem:
        nums_min = elem

print(nums_max, nums_min)