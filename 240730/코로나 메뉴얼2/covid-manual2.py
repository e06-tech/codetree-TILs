result = [0]*4 #결과 저장할 배열
#결과 저장하는 배열이 for문 내에 있으면 안 된다!!!

for i in range(3):
    sym1, sym2 = input().split()
    
    sym2 = int(sym2) #정수 정보는 정수로 변환

    if sym1 == 'Y' and sym2 >= 37:
        result[0] += 1
    elif sym1 == 'N' and sym2 >= 37:
        result[1] += 1
    elif sym1 == 'Y' and sym2 < 37:
        result[2] += 1
    else:
        result[3] += 1

if result[0] >= 2:
    result.append('E')

print(*result)
#for elem in array:
    #print(elem, end=' ')
#의 형식이어도 된다. 어느 쪽이든 편한 대로 할 것.