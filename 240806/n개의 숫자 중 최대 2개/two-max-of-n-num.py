n = int(input())

nums = list(map(int, input().split()))

m1 = m2 = min(nums)
#간단하게 sorting 함수 써서 정렬시키는 방식도 있지만 일단은 하나하나 해 보고 싶어서 아래와 같이 풂.
#min 값으로 지정 안 하고 임의의 정수, 혹은 배열 내 특정 원소값으로 지정할 경우 
#임의의 정수 지정 -> 그 값이 배열 내 최댓값보다 클 때 최댓값 찾기 실패
#배열 내 특정 원소값 지정 -> 그 값이 배열 내 최댓값일 때 m2가 제대로 출력되지 않는 문제가 생김

for i in range(len(nums)):
    if m1 <= nums[i]:
        m1 = nums[i]

nums.remove(m1)
#단순히 nums.remove(nums[i])로 코드를 짤 시 배열의 맨 마지막 원소만 삭제되는 대참사 발생

for j in range(len(nums)):
    if m2 <= nums[j]:
        m2 = nums[j]

print(m1, m2)