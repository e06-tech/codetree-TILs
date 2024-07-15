n = int(input())

array = list(map(int, input().split()))

new_array = [elem**2 for elem in array]

for i in range(n):
    print(new_array[i], end=' ')
    #n을 받긴 했어도 리스트 길이지정을 안 썼다. 
    #그냥 들어오는 정수를 바로 받아서 리스트로 만드는 방법을 썼지.
    #그래서 n을 과연 쓸 일이 있을까 했더니 여기서 써먹네 ㅎㅎㅎ