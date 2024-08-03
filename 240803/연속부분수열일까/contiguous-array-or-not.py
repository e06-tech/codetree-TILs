n1, n2 = map(int, input().split())
#사실 n1, n2를 거의 쓸 일은 없지만..
#for 문에서 넣을까 했으나 통일성 있게 코드를 짜는 과정에서 쓰지 않았다.

A = list(map(int, input().split()))
B = list(map(int, input().split()))
#일단 리스트 A, B 완성

flag = 0
for i in range(len(A) - len(B)+1):
    mod_A = A[i:i+len(B)]
    if mod_A == B:
        flag = 1
        break

if flag == 1:
    print("Yes")
else:
    print("No")