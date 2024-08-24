#문자열이 한 줄에 하나씩 총 n개 -> 이 경우에 적용해 볼 수 있는 코드!

n = 4
arr = [
    input()
    for _ in range(n)
]
#이 코드는 그냥 외워 버리자. 일일이 append 치기도 좀 귀찮다...

for i in range(4):
    print(arr[3-i])