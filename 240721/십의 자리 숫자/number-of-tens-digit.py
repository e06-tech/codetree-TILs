#key point: 0은 항상 배열의 맨 마지막!

array = list(map(int, input().split()))
number = [0]*10

for i in range(len(array)):
    array[i] = array[i]//10
    #이러면 0 직전까지는 십의 자릿수 출력해서 교체 완료!

for elem in array:
    number[elem] += 1

for j in range(1, 10):
    print(j, "-" , number[j])

#휴... 역시 필기시험+대청소+기차 타고 장거리 이동까지 한 날은 밤늦게 문제 풀어보자고 하는 거 아니다...