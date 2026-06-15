"""7_1"""
# # tuple assignment에 관한 내용
# import math
# radius = float(input("원의 반지름을 입력하시오: "))
# def calC (r):
#     A = math.pi * r * r
#     S = 2 * math.pi * r
#     return (A,S)
# (a,b) = calC(radius)
# print(f"원의 넓이는 {a}이고 원의 둘레는 {b}이다. ")
"""
set 관련 명령어
set(): 비어있는 set 생성
len(set): set의 크기
set은 집합이므로 자동으로 중복요소를 제거함 
set(리스트 or 문자열): 리스트나 문자열로부터 set을 생성한다
set.add(element): set에 요소 추가
set.discard(element): 요소 삭제
set.clear(): 세트를 빈 세트로 초기화
set1.union(set2): 합집합 세트 반환
set1.intersection(set2): 교집합 세트 반환
set1.difference(set2): set1-set2 세트 반환

"""
"""7_1"""
# partya = set(['Kim', 'Park', 'Lee'])
# partyb = set(['Choi', 'Park'])
# intersection = partya.intersection(partyb)
# print (f"동시에 참석한 사람: {intersection}")
"""7_2"""
# ss = str(input("문자열을 입력하시오: "))
# setss = set(ss.split())
# print(f"중복되지 않은 단어의 개수: {len(setss)}")

"""
dictionary--> key:value pair. key를 이용하여 value를 찾음. 
공백 딕셔너리의 생성: {}
ex) contacts = {'Kim':'01012345678', 'Park':'01012345679', 'Lee':'01012345680’}
contacts['Kim'] == contacts.get('Kim') == '01012345678'이 되는 것!
key가 없을 때, 새로운 pair를 추가하고 싶어도 여전히 get을 쓰면 됨!
contacts.get('Choi', 앞의 것이 없을 때 추가할 value) 이런식으로 하면 새로운 pair가 추가됨.
아니면 contacts['Choi'] = '01014245453' 이런식으로 하면 됨
삭제: contacts.pop('Kim')으로 하면 value 값이 반환되며 pair가 삭제됨.

"""
"""7_3"""
# english_dict = dict()
# english_dict['one'] = '하나'
# ans = str(input("단어를 입력하시오: "))
# print(english_dict.get(ans, '없음'))
"""7_4"""
# emailid = str(input("이메일 주소를 입력하시오: "))
# splited = emailid.split("@")
# print(f'''아이디: {splited[0]}
# 도메인: {splited[1]}''')

"""7_5(겁나중요)"""
# ss = str(input("암호화할 문자열을 입력하세요: "))
# shift = int(input("암호화에 사용할 시프트 값을 입력하세요 (양수 또는 음수): "))
# encrypted = ""
# for i in ss:
#     if i.isalpha():
#         if i.islower():
#             encrypted += chr((ord(i)-ord('a')+shift)%26+ord('a'))
#         else:
#             encrypted += chr((ord(i)-ord('A')+shift)%26+ord('A'))
#     else:
#         encrypted += i
# print(f"암호화된 문자열: {encrypted}")

"""7_6"""
# ss = str(input("문자열을 입력하시오: "))
# wordlist = list(ss.lower().split())
# words = {}
# for i in wordlist:
#     if i in words:
#         words[i] += 1
#     else:
#         words[i] = 1
# for text, count in words.items():
#     print(f"'{text}': {count}번")