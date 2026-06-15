"""4_2"""
# k = int(input("정수를 입력하세요. "))
# factorial = 1
# for i in range (k):
#     factorial = factorial * (i+1)
# print(f"{k}!은 {factorial}이다.")
"""4_5"""
# print("종료하려면 음수를 입력하세요.")
# i = 0
# sum = 0
# seq = 0
# while i >= 0:
#     i = int(input("성적을 입력하시오: "))
#     if i >= 0:
#         sum += i
#         seq += 1
# print(f"성적의 평균은 {sum/seq}점입니다.")
"""4_6"""
# ans = ""
# words = []
# while ans != "quit":
#     ans = str(input("단어를 입력하세요 ('quit'으로 종료)"))
#     if ans != "quit":
#         words.append(ans)
# print(f"입력된 단어 개수: {len(words)}\n입력된 단어 목록: {words}")
"""4_7"""
# x = int(input("정수를 입력하시오(큰수): "))
# y = int(input("정수를 입력하시오(작은수): "))
# while y != 0: 
#     r = x % y
#     x , y = y , r
# print(f"최대 공약수는 {x}입니다.")
"""4_9"""
# raw = str(input("문자열을 입력하시오: "))
# count = [0,0,0]
# for i in raw:
#     if i.isalpha():
#         count[0] += 1
#     elif i.isdigit():
#         count[1] += 1
#     elif i.isspace():
#         count[2] += 1
# print(f'''알파벳 문자의 개수: {count[0]}
# 숫자 문자의 개수: {count[1]}
# 스페이스 문자의 개수: {count[2]}''')
"""5_4"""
# import random
# def generate():
#     keyboard = "abcdefghijklmnopqrstuvwxyz0123456789"
#     password = ""
#     for i in range (6):
#         password += keyboard[random.randint(0,len(keyboard)-1)]
#     return password

# for j in range (3):
#     print (generate())
"""5_8(split 명령어 외우자)"""
# def analyze_string(text):
#     a = len(ss)
#     b = len(ss.split(" ")) 
#     return a, b
# ss = str(input("명령어를 입력하세요: "))
# result_length , result_count = analyze_string(ss)

# print(f"문자열 길이: {result_length}")
# print(f"단어 개수: {result_count}")
