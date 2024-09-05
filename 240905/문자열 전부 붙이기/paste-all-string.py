n = int(input())
words = [
    input()
    for _ in range(n)
]
total_str = ""

for elem in words:
    total_str = total_str + elem

print(total_str)