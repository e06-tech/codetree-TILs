n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

sum = 1

for i in range(n):
    for j in range(m):
        arr[i][j] = sum
        sum += 1

for row in arr:
    for elem in row:
        print(elem, end = ' ')
    print()