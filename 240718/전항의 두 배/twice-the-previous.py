A1, A2 = map(int, input().split())
array = []
array.append(A1)
array.append(A2)

for i in range(2, 10):
    x = array[i-1] + 2*array[i-2]
    array.append(x)

for j in range(len(array)):
    print(array[j], end = ' ')