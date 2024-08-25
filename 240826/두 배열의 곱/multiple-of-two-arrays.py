arr_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
"""for k in range(3):
    arr_1.append(list(int, input().split()))"""

input()
#input들 사이에 한 줄의 공백이 있는 경우 이걸 안 넣어 주면 오류가 난다!

arr_2 = [
    list(map(int, input().split()))
    for _ in range(3)
]
"""for m in range(3):
    arr_2.append(list(int, input().split()))"""

arr_3 = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr_3[i][j] = arr_1[i][j]*arr_2[i][j]

for row in arr_3:
    for elem in row:
        print(elem, end = ' ')
    print()