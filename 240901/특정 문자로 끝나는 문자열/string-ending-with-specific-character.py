words = [
    input()
    for _ in range(10)
]
letter = input()

words_end_with_letter=[]

for elem in words:
    if elem[-1] == letter:
        words_end_with_letter.append(elem)

if len(words_end_with_letter) == 0:
    print('None')
else:
    for i in range(len(words_end_with_letter)):
        print(words_end_with_letter[i])