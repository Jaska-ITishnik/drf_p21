# single_digit_numbers = {
#     1: "One",
#     2: "Two",
#     3: "Three",
#     4: "Four",
#     5: "Five",
#     6: "Six",
#     7: "Seven",
#     8: "Eight",
#     9: "Nine"
# }
#
# double_numbers_dict = {
#     10: "ten",
#     20: "twentee",
#     30: "thirtee",
#     40: "fortee",
#     50: "fiftee",
#     60: "sixtee",
#     70: "seventee",
#     80: "eightee",
#     90: "nintee"
# }
#
# number_words = [
#     "Hundred",
#     "Thousand",
#     "Million",
#     "Billion"
# ]
# num = 2145362987
# res = ''
# if (a := num // 1000000000) > 0:
#
#     res += f"{single_digit_numbers[a]} {number_words[3]}"
#     num = num % 1000000000
#
# if (a := num // 1000000) > 0:
#     res += f"{single_digit_numbers[a]} {number_words[2]}"
#     num = num % 1000000
#
# if (a := num // 1000) > 0:
#     res += f"{single_digit_numbers[a]} {number_words[1]}"
#     num = num % 1000
#
# if (a := num // 100) > 0:
#     res += f"{single_digit_numbers[a]} {number_words[0]}"
#     num = num % 100
#
# print(res)
from collections import Counter

# class IsHandler:
#     def __init__(self, id):
#         self.id = id
#         id += 50
# obj = IsHandler(11)
# print(obj.id)

# for i in range(10):
#     if i == 5:
#         break
#     else:
#         print(i)
# else:
#     print('Python')

# def f():
#     yield 55
#     yield 2
#     yield 3
# fun = f()
# print(next(fun))
#
# print(10)
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# n = int(input('How many numbers:'))
# print(*fibonacci(n))


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# a = []
# b = []
# for i in range(1, len(strs)):
#     for j in range(i, len(strs)):
#         if set(strs[i - 1]) == set(strs[j]):
#             a.append()