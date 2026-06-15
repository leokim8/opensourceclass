"""
list 와 관련된 함수
list.insert(n,"element") : 인덱스 n의 자리가 element이 되도록 element를 리스트에 끼워넣음
list.index("element"): element가 리스트에 처음 등장하는 인덱스를 추출함. 
list.pop(n) : 인덱스 n의 element를 list에서 빼고, 그 element를 return함. n값이 주어지지 않으면, 마지막 element에 대해 이를 수행. 
list.remove("element"): element를 list에서 뺌. 
list.count("element"): list에 element가 몇 개 있는 지 셈. 
list.sort(): list를 정렬함. 
min(list): list 속 최소값 반환
max(list): list 속 최댓값 반환
sorted(list, key=str.lower 등,reverse=True/False): list를 sort한 값을 반환해줌. key: sort하는 파라미터, reverse: 역순으로 할 지 말 지 정해줌
list copy하고 싶으면: list2 = list(list1)으로 ㄱㄱ
list2 = [출력식, for 입력 리스트에 있는 요소 in 입력 리스트]

"""
"""6_2"""
# doglist = []
# ans = "answer"
# while ans != "":
#     ans = str(input("강아지의 이름을 입력하시오(종료시에는 엔터키) "))
#     if ans != "":
#         doglist.append(ans)
# print("강아지들의 이름: \n")
# for i in doglist:
#     print(i, end = ", ")
"""6_5"""
# row = 6
# col = 6
# numlist = []
# for i in range(row):
#     numlist += [[0]*col]

# for i in range(row):
#     for j in range(col):
#         numlist[i][j] = i+j+2
# print(numlist)
