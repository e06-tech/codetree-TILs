n = int(input())

arrary = list(map(int, input().split()))
even = []

for i in range(n):
    if arrary[i]%2 == 0:
        even.append(arrary[i])

for i in range(len(even)):
    print(even[i], end=' ')