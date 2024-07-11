T = list(map(int, input().split()))

filtered_T = T[1::2]
filtered_T_3 = T[2::3]

total = 0
aver = 0

for i in range(5):
    total = total + filtered_T[i]

for i in range(3):    
    aver = filtered_T_3[i] + aver

aver = aver/3

print(total, aver)