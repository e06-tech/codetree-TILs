word, letter = input().split()

if letter in word:
    print(word.index(letter))
else:
    print('No')