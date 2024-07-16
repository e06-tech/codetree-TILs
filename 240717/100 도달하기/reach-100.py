n = int(input())

array = []

array.append(1)
array.append(n)
#여기까지가 1, n을 제 1항/2항으로 지정하는 부분.

i = 0
while True:
    array.append(array[i]+array[i+1])
    if array[i+2]>100:
        break
    i = i+1

for i in range(len(array)):
    print(array[i], end = ' ')