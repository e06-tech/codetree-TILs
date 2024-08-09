#바로 직전에 푼 문제의 코드 응용하면 쉽다.
#이것도 코드 겹쳐쓰기 사용하면 된다.
#관건: 동일 원소-동일 원소, 즉 gaps[1]-gaps[1] 같은 경우를 어찌할 것인가?
# -> j의 범위를 [i+1]대신 [i]로만 설정해 주면 된다!
#(어차피 숫자는 오름차순으로 주어지므로 절댓값 이런 건 신경쓸 필요 x)

n = int(input())

numbers = list(map(int, input().split()))
gaps = []

for i in range(n):
    for j in range(i):
        gaps.append(numbers[i]-numbers[j])

print(min(gaps))