n = int(input())

words = [
    input()
    for _ in range(n)
]

letter = input()
total = 0
list_total = []

for elem in words:
    if elem[0] == letter:
        total = total + len(elem)
        list_total.append(elem)

answer = total/len(list_total)

print(len(list_total),'%0.2f'%answer)