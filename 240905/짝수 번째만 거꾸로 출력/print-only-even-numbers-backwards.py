word = input()
word_even = []
for i in range(len(word)):
    if i%2 == 1:
        word_even.append(word[i])

for j in range(len(word_even)-1, -1, -1):
    print(word_even[j],end='')