n,m = map(int, input().split())

element = 0

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(m):
    if i%2 == 0:
        for j in range(n):
            arr[j][i] = element
            element += 1
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = element
            element += 1
        
for row in arr:
    for elem in row:
        print(elem, end = ' ')
    print()