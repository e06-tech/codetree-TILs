n = 10
result = list(map(int, input().split()))

result_array = [0]*7

for elem in result:
    result_array[elem] += 1

for i in range(1, 7):
    cnt = result_array[i]
    print(i, "-" ,cnt)
    #문제에서는 다른 print함수 형식의 코드로 작성함.
    #다만, 여기서는 그 형식으로 작성했을 시 에러가 발생해서 정수와 str을 혼합하는 다른 방식으로 작성.