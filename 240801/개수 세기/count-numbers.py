n, m = map(int, input().split())
#사실 이 코드에서 n은 크게 필요 x. 들어오는 수는 list형식으로 다 받으니까.

num_list = list(map(int, input().split()))
cnt = num_list.count(m)

print(cnt)