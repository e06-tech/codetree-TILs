words = input()

l = len(words)
answer = ['No', 'No']

for i in range(l-1):
    if words[i:i+2] == 'ee':
        answer[0] = 'Yes'
    else:
        pass

for i in range(l-1):
    if words[i:i+2] == 'ab':
        answer[1] = ('Yes')
    else:
        pass

print(*answer)