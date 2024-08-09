numbers = list(map(int, input().split()))

below = 0
above = []

for elem in numbers:
    # 500 미만의 수 중 가장 큰 수 찾기
    if below < elem and elem < 500:
        below = elem

for elem in numbers:
    # 500 초과의 수 중 가장 큰 수 찾기
    if elem > 500:
        above.append(elem)

print(below, min(above))

#간단하게 후룩 풀린 문제!