score = list(map(int, input().split()))
i = 0
report = [0]*11

while True:
    if score[i] != 0:
        i += 1
        continue
    else:
        break

score = score[:i]
#0점은 어차피 최종 카운팅에서 제외

for k in range(len(score)):
    score[k] = score[k]//10
    #10의 자릿수 분리

for elem in score:
    report[elem] += 1
    #해당 점수대에 해당하는 학생수 카운팅

for j in range(10, 0, -1):
    print((j)*10, "-", report[j])
    #점수대 출력
    #**리스트 범위를 거꾸로 잡고 출력하는 것에 약하다. 다시 복습하자!