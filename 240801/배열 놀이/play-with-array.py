n, q = map(int, input().split())
#n, q 정보 입력

array = list(map(int, input().split()))

for i in range(q):
    list_x = list(map(int, input().split()))
    #각 질의는 번호로 구분됨. 여기서는 각 리스트의 맨 첫번째 원소가 질의의 종류를 구분하는 번호.
    if list_x[0] == 1:
        a = list_x[1]
        print(array[a-1])

    elif list_x[0] == 2:
        b = list_x[1]
        inx = -1 
        #idx 감지를 위한 표지판
        
        idx = 0
        #index를 출력하고 싶으면 'idx'라고 똑바로 입력할 것. inx 등으로 오타 내면 안 된다!
        for elem in array:
            if elem == b:
               idx = array.index(b)
               inx = 1
               break
            
        if inx == -1:
            print(0)
        else:
            print(idx+1)
        #inx가 -1로 남아 있다 -> 맞는 원소 없음. 0 출력.
        #inx가 -1이 아니다 -> 맞는 원소 있음. index 정보 출력.


    else:
        s = list_x[1]
        e = list_x[2]
        array_mod = array[s-1:e]
        print(*array_mod)

        #key point: 배열은 0부터 카운팅되나, 문제에서 원하는 답은 사람이 셀 때처럼 1번째, 2번째.. 식으로 출력되는 것.
        #따라서 그에 맞게 +1, -1 등의 위치 조정을 적절히 해 줘야 한다!