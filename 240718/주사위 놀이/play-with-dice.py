n = 10
result = list(map(int, input().split()))

result_array = [0]*7

for elem in result:
    result_array[elem] += 1

for i in range(1, 7):
    cnt = result_array[i]
    print(print("{i} - {cnt}"))