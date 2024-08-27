n, m = map(int, input().split())

arr_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr_1[i][j] != arr_2[i][j]:
            result[i][j] = 1
        else:
            result[i][j] = 0

for row in result:
    for elem in row:
        print(elem, end=' ')
    print()

"""for row in arr_1:
    for elem in row:
        print(elem, end=' ')
    print()

for row in arr_2:
    for elem in row:
        print(elem, end=' ')
    print()"""
# arr_1, arr_2 확인용