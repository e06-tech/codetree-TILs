arr = input().split()
total = 0

for i in range(10):
    total = total + len(arr[i])

print(total)