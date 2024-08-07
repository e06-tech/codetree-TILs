N = int(input())

nums = list(map(int, input().split()))
nums.sort()
#배열 nums 정렬

nums_selected = []
for i in range(len(nums)):
    if i == 0 or i == len(nums)-1:
        if nums[0] != nums[1]:
            nums_selected.append(nums[0])
        if nums[len(nums)-1] != nums[len(nums)-2]:
            nums_selected.append(len(nums)-1)
        
    else:
        if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
            nums_selected.append(nums[i])
#중복되지 않는다 = 양쪽의 숫자와 모두 일치하지 않는다!! (단, 양끝은 각자의 왼/오와 불일치하면 되므로 예외)

print(nums_selected[-1])