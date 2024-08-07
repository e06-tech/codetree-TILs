N = int(input())

nums = list(map(int, input().split()))
nums.sort()
#배열 nums 정렬

nums_selected = []
for i in range(N):
    if i == 0: 
        if nums[0] != nums[1]:
            nums_selected.append(nums[0])
    if i == N-1:
        if nums[N-1] != nums[N-2]:
            nums_selected.append(nums[N-1])
    #if-elif-else구조로 짜지 말 것! if-elif 구조를 적용하면 i==N-1일 경우를 그대로 지나쳐 버리기 때문에 쓸데없는 오류만 생기고 더 힘들어진다!    
    # (else로 바로 넘어가 버리기 때문에 오류 발생)
    if i != 0 and i != N-1:
        #else로 하려 했으나 if로 변경. else로 둘 시 i==0일 때 if문을 한 번 더 거치고도 또 다른 if-else문을 만나는 것이기에 중복으로 잡힌다!
        if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
            nums_selected.append(nums[i])
#중복되지 않는다 = 양쪽의 숫자와 모두 일치하지 않는다!! (단, 양끝은 각자의 왼/오와 불일치하면 되므로 예외)

if len(nums_selected) != 0:
    print(nums_selected[-1])
else:
    print(-1)
#으아... 눈 빠지게 중복되는 원소 제거하고 범위 내 최대 원소 잡는 코드만 짜다가 정작 중요한 걸 놓쳤다...