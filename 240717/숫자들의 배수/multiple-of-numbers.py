n = int(input())
i = 1
times = []

while (len(times) != 2):
    print(n*i, end = ' ')
    if (n*i)%5 == 0:
        times.append(n*i) 

    i = i + 1