A = list(map(int, input().split()))
B = list(map(int, input().split()))
#일단 리스트 A, B 완성

flag = 0
for i in range(len(A) - len(B)+1):
    A[i:i+len(B)] = mod_A
    if mod_A == B:
        flag = 1
        break

if flag == 1:
    print("Yes")
else:
    print("No")