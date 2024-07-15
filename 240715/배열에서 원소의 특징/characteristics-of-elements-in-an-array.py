array = list(map(int, input().split()))
i = 0

while True:
    if array[i]%3 != 0:
        i = i + 1
        continue
    else:
        break

print(array[i-1])