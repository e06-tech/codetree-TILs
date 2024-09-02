words = input()
n = int(input())

for i in range(len(words)-1, len(words)-n-1, -1):
    print(words[i], end='')