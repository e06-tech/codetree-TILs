n = int(input())
cycle = 1
#n 가지고 10의 자리, 1의 자리 한 번 분리해 주는 것만으로도 기본 사이클 1회 돌아감.
a = n // 10
b = n%10
#여기서 a, b 계산은 미리 해 줘야 함. while문 안으로 계산을 집어넣을 시 무한 뺑뺑이가 돎.

while(1):
    c = a + b
    d = b*10 + c%10
    if d != n:
        cycle = cycle + 1
        a = d // 10
        b = d % 10
        continue
    else:
        break

print(cycle)