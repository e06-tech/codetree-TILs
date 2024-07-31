results = []
a, b = map(int, input().split())

while a >= 1:
    c = a%b
    results.append(c)
    a = a//b

results.sort()
#테스트 케이스에서는 해당 코드가 없어도 통과. 그러나 (50,3)이라는 케이스를 고려하면 왜 있어야 하는지 알게 됨.

results_num = [1]

for i in range (1, len(results)):
    if results[i] == results[i-1]:
        results_num[-1] = results_num[-1] + 1
    else:
        results_num.append(1)

sum = 0

for elem in results_num:
    sum += elem**2

print(sum)

#이틀 정도 고민하니까 풀리긴 풀리네..?
#일상생활 중에 무의식적으로 고민하는 방법이 확실히 도움이 된다.