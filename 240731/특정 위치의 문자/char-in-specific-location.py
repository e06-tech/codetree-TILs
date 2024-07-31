T = ['L', 'E', 'B', 'R', 'O', 'S']

letter = input()
idx = -1 #일치하는 문자가 없을 시 -1 출력

for i, char in enumerate(T):
    if char == letter:
        idx = i
        print(idx)
        break

if idx == -1:
    print('None')