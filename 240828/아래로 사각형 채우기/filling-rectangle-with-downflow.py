n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
] #2차원 배열 만드는 기본 코드 (shallow 배열 안 만드려면 이렇게 할 것)

for i in range(n):
    arr[i][0] = i+1
    for j in range(1,n):
        arr[i][j] = i+1 + j*n

for row in arr:
    for elem in row:
        print(elem, end = ' ')
    print()