"""8_1"""
# class bankaccount():
#     def __init__ (self):
#         self.__balance = 0
#     def withdraw(self,money):
#         self.__balance -= money
#         print(f"통장에서 {money}가 출금되었음")
#         return self.__balance
#     def deposit(self,money):
#         self.__balance += money
#         print(f"통장에서 {money}가 입금되었음")
#         return self.__balance

# a = bankaccount()
# a.deposit(10)
# a.withdraw(1)

"""8_2"""
# class Cat():
#     def __init__ (self, name, age):
#         self.__name = name
#         self.__age = age
#     def setname(self, name):
#         self.__name = name
#     def setage(self,age):
#         self.__age = age
#     def getname(self):
#         return self.__name
#     def getage(self):
#         return self.__age

# a = Cat("Missy", 3)
# b = Cat("Lucky", 5)

# print(f"{a.getname()} {a.getage()}")
# print(f"{b.getname()} {b.getage()}")
    
"""8_3"""
# class Student():
#     def __init__ (self, name, age):
#         self.__name = name
#         self.__age = age
#     def __lt__(self, other):
#         return self.__age < other.__age

# s1 = Student("Kim", 20)
# s2 = Student("Lee", 22)

# print (s1 < s2)
# print (s1 > s2)

"""8_추가"""
# class Student():
#     def __init__ (self):
#         self.__name = ""
#         self.__num = 0
#     def whatsyourname (self):
#         self.__name = input("이름이 뭐임?: ")
#     def whatsyournum (self):
#         self.__num = int(input("학번이 뭐임?: "))
#     def printit (self):
#         print(f"이름: {self.__name}, 학번: {self.__num}")


# a = Student()
# a.whatsyourname()
# a.whatsyournum()
# a.printit()