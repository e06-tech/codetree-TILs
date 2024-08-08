#최댓값 찾고, 그 위치인 i를 출력케 하되
#array[:i]와 그 길이를 측정하는 변수를 따로 두고
#i = 1일 때, 즉 배열의 길이가 1일 때 반복문이 종료되게 한다.
#한 번 최댓값을 찾고 나면 array[:i] 범위 내에서 찾으면 될 것이고.

N = int(input())
leng = N
array = list(map(int, input().split()))
record = []

while True:
    array_mod = array[:leng] #길이에 맞게 배열 정리
    a = max(array_mod)
    
    for i in range(len(array_mod)):
        if a == array_mod[i]:
            break
        else:
            continue  

    record.append(i+1)

    if i == 0:
        break
    else:
        pass

    leng = i

print(*record)