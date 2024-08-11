for _ in range(5):
# 주어진 문자열
    input_string = input()

# 문자열을 공백을 기준으로 나누고 각 단어를 대문자로 변환한 후 다시 합치기
    uppercase_string = ' '.join([s.upper() for s in input_string.split()])

    print(uppercase_string)