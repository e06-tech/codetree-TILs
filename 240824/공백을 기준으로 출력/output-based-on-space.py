list_a = list(input().split())
list_b = list(input().split())

base = list_a[0]

for j in range(1,len(list_a)):
    base = base + list_a[j]

for i in range(len(list_b)):
    base = base + list_b[i]

print(base)