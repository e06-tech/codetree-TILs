word = input()
l = len(word)

count_ee = 0
count_eb = 0

"""for i in range(l-1):
    if word[i:i+1] == "ee":
        count_ee += 1
    else:
        pass

for j in range(l-1):
    if word[j:j+1] == "eb":
        count_eb += 1
    else:
        pass

print(count_ee, count_eb, end=' ')"""
# 이 코드는 작동 안 되는 코드. 이유는 모르겠다.#

if 'ee' in word:
    count_ee += 1

if 'eb' in word:
    count_eb += 1

print(count_ee, count_eb, end=' ')