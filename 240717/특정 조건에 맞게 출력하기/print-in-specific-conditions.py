array = list(map(int, input().split()))
array2 = []
i = 0

while True:
    if array[i] != 0:
        array2.append(array[i])
        i = i + 1
        continue
    else:
        break

#array2: 0이 아닌 부분까지의 숫자를 담은 배열

for j in range(len(array2)):
    if array2[j]%2 == 1:
        array2[j] = array2[j] + 3
    else:
        array2[j] = array2[j]//2

for m in range(len(array2)):
    print(array2[m], end = ' ')