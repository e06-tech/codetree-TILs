nums = list(map(int, input().split()))
#일단, 들어오는 숫자는 다 받는다.
tens = [0]*10
i = 0

while True:
    if nums[i] != 0:
        i += 1
        continue
    else:
        break

nums = nums[:i]

for elem in nums:
    elem = elem//10
    tens[elem] += 1

for j in range(1, 10):
    print(j, "-", tens[j])