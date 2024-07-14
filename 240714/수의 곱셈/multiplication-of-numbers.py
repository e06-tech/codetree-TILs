x, y, z = map(int, input().split())

A = x*y
B = x*z
C = y*z
D = x*y*z
#이렇게 지정 안 하고 cal리스트 안에 계산식을 그대로 집어넣을 수도 있다.
#하지만 실수할 가능성이 높아지니 능숙해지기 전까지는 안 그러는 걸로.

cal = [x, y, z, A, B, C, D]

odd = [0]*len(cal)
even = [0]*len(cal)

for i in range(len(cal)):
    if cal[i]%2 == 1:
        odd[i] = cal[i]
    else:
        even[i] = cal[i]

if max(odd) == 0:
    print(max(even))
else:
    print(max(odd))