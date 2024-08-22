len_str1 = len(input())
len_str2 = len(input())
len_str3 = len(input())

lens = [len_str1, len_str2, len_str3]

a = min(lens)
b = max(lens)

print(b - a)