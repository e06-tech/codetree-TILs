array = [0]*10
array[0], array[1] = map(int, input().split())

for i in range(2, 10):
    array[i] = (array[i-1] + array[i-2])%10

for i in range(0, 10):
    print(array[i], end = " ")