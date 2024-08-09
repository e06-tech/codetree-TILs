#for문 겹쳐쓰기를 통해 풀면 쉽다
#(그리고 또다시 절절히 느끼는 것: 머리 아플 때는 코딩하는 거 아니다!)

n = int(input())

price = list(map(int, input().split()))
profit = []
profit_max = 0

for i in range(n):
    for j in range(i+1):
        profit.append(price[i]-price[j])   
#n년간 각각의 차값 변동에 대한 이익 분석.
#그 해에 사서 그 해에 파는 것도 포함     

for elem in profit:
    if elem > profit_max:
        profit_max = elem
#이익의 최댓값 구하기

print(profit_max)