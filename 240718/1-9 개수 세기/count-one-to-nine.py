n = int(input())
array = list(map(int, input().split()))

count_array = [0]*(10)
#주어진 수가 몇 번 나왔는지 카운트하기용

for elem in array:
    count_array[elem] += 1

for i in range(1, 10):
    print(count_array[i])