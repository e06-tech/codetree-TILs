n = int(input())

words = [
    input()
    for _ in range(n)
]

a_total = 0
length = 0

for elem in words:
    if elem[0] == 'a':
        a_total += 1

for elem in words:
    length = length + len(elem)

print(length, a_total)