T = list(map(int, input().split()))
total = 0

for i in range(len(T)):
    if T[i] != 0:
        continue
    else:
        break

total = T[i-1] + T[i-2] + T[i-3]

print(total)