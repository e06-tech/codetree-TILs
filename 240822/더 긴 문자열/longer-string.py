input1, input2 = input().split()

len1 = len(input1)
len2 = len(input2)

if len1 > len2:
    print(input1, len1)
elif len1 < len2:
    print(input2, len2)
else:
    print('same')