words = input()
n = int(input())

if n <= len(words):
    for i in range(len(words)-1, len(words)-n-1, -1):
        print(words[i], end='')
else:
    for i in range(len(words)-1, -1, -1):
        print(words[i], end='')