words =["apple", "banana", "grape", "blueberry", "orange"]
targets = []

letter = input()

for elem in words:
    for i in range(2,4):
        if letter == elem[i]:
            targets.append(elem)

for item in targets:
    print(item, end='\n')

print(len(targets))