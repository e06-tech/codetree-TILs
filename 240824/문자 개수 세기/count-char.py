string = input()
letter = input()
count = 0

for elem in string:
    if elem == letter:
        count += 1

print(count)