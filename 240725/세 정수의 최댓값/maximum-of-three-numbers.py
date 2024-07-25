a, b, c = map(int, input().split())

# 사실 맘 같아선 세 수 전부 list로 받은 다음에 max 함수 써버리고 싶지만..
# 문제에서 제시한 조건을 따라야겠지.  

if a > b:
    if a > c:
        print(a)
    elif a < c:
        print(c)

elif a > c:
    if a > b:
        print(a)
    elif a < b:
        print(b)

elif b > a:
    if b > c:
        print(b)
    elif b < c:
        print(c)

elif b > c:
    if b > a:
        print(b)
    elif b < a:
        print(a)

elif c > a:
    if c > b:
        print(c)
    elif c < b:
        print(b)

else:
    if c > a:
        print(c)
    elif c < a:
        print(a)
# c>b인 경우. else라 조건은 굳이 쓰지 않았다.