a, b = map(int, input().split())

A = a**b
B = b**a

if A > B:
    print(A - B)
elif A < B:
    print(B - A)
else:
    print(0)