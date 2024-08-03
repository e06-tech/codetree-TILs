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

#for 문 형식으로 for elem range nums를 쓸 수도 있다.
#단, 이 경우에는 '2'라는 원소가 여러 개 있기 때문에 idx로 가장 작은 수를 출력한다.
#즉, 3번째 2가 나오는 경우에 대한 인덱스를 출력하지 않는다!