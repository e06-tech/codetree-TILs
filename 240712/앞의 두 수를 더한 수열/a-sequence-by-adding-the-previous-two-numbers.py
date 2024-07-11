#피보나치 수열을 파이썬으로 구현

n = int(input())
T = [0]*(n+1)

T[0] = 0
T[1] = 1

for i in range(2,n+1):
    T[i] = T[i-2]+T[i-1]

print(T[n])