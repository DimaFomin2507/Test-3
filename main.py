#
# def func():
#     yield 1
#     yield 2
#     yield 3
#
# s = func()
# print(next(s))
# print(next(s))
# print(next(s))

import json


# import time


# №2

# text = """Всем привет как дела тра та та"""
# pure_text = text.lower().replace('', '')
# letters = {
#     letter: pure_text.count(letter)
#     for letter in set(pure_text)
# }
# print(letters)


# 29.11.23

# №1
# names = [
#     ('Саша', 'Петров'),
#     ('Дима', 'Яковлев')
# ]
# last_names = [
#     last_name
#     for _, last_name in names
#     if 'п' in last_name.lower()
# ]
# print(last_names)

# №2
# lst = list(range(10))
# lst1 = []
# for number in lst:
#     if not number % 2:
#         lst1.append(number)
# lst2 = [n for n in lst if not n % 2]
# print(lst2)

# №3
# student = [
#     {"name": "Саша", "mark": 5},
#     {"name": "Женя", "mark": 4},
#     {"name": "Павел", "mark": 2}
# ]
# lst = [
#     student["name"]
#     for student in student
#     if student["mark"] != 2
# ]
# print(lst)

# numbers = [2, 6, 8, 9, 3, 2, 7, 1]
# def is_simple(number: int) -> bool:
#     """
#     Функция, которая определяет число простое или нет
#     :param number: Само число
#     :return: Булево значение
#     """
#     for i in range(2, number):
#         if not number % i:
#             return False
#     return True
# print([n for n in numbers if is_simple(n)]


# students = [
#     {"name": "Саша", "mark": (2, 4)},
#     {"name": "Женя", "mark": (4, 5)}
#  ]
# with open("test2.json", "w", encoding='utf-8') as f:
#     json.dump(students, f, ensure_ascii=False)
# with open("test2.json", "r", encoding='utf-8') as f:
#     students2 = json.load(f)
#     new_students = []
#     for student in students2:
#         student['mark'] = tuple(student['mark'])
#         new_students.append(student)
# print(new_students)
#
#
#
#
#
#
# json


# 04.12.23

# def range1(a: int, b=None, step=1):
#     if not b:
#         b, a = a, 0
#     number = a
#     while number < b:
#         yield number
#         number += step
# print(list(range(8)))
# print(list(range1(8)))


# def func(name: str, no_middle=False) -> str:
#     l, f, m = name.split()
#     return f"{l} {f[0]}." + (f"{m[0]}." if no_middle else "")
#     # first_name = lst[0]
#     # middle_name = lst[1]
#     # lat_name = lst[2]
#     # print(first_name + ' ' + middle_name[0] + '.' + lat_name[0] + '.')
#
# print(
#     func("Ванин Иван Иванович"),
#     func("Ванин Иван Иванович", no_middle=True),
#     sep='\n'
# )


# from  datetime import datetime
# import time
# def dec(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         result = func(*args, **kwargs)
#         time.sleep(1)
#         print(datetime.now() - start)
#         return result
#     return wrapper
# @dec
# def p(a):
#     print(a)
# p(2)


# def f1(number):
#     def f2():
#         print(number)
#     return f2
# s1 = f1(5)
# s2 = f1(6)
# s1()
# s2()


# n = "1234 1234 1234 5678"
# "**** **** **** 5678"
# def p(n):
#     l = len(n)
#     if l > 4:
#         s = '*' * (l - 4)
#     else:
#         s = ''
#     return s + n[-4:]
# print(p(n))


# 25.12.2023

class BaseFileHandler:
    def __init__(self, path: str):
        self._path = path

    def read(self) -> dict:
        with open(self._path, 'r', encoding='utf-8') as f:
            return self._deserialize(f.read())

    def _deserialize(self, data: str) -> dict:
        return {}

    def write(self, data: dict):
        with open(self._path, 'w', encoding='utf-8') as f:
            f.write(self._serialize(data))

    def _serialize(self, data: dict) -> str:
        return ''


class TXTFileHandler(BaseFileHandler):
    def __init__(self, path, key_sep="=", pair_sep="\n"):
        super().__init__(path)
        self.ks = key_sep
        self.ps = pair_sep

    def _serialize(self, data: dict) -> str:
        return '\n'.join(
            f"{key}={value}" for key, value in data.items()
        )

    def _deserialize(self, data: str) -> dict:
        return {key: value
                for key, value in [line.split('=')
                                   for line in data.split('\n')]
                }


class TextFileHandler(BaseFileHandler):
    def _serialize(self, data: dict) -> str:
        return ','.join(
            f"{key}:{value}" for key, value in data.items()
        )

    def _deserialize(self, data: str) -> dict:
        return {key: value
                for key, value in [line.split(':')
                                   for line in data.split(',')]
                }


class JSONFileHandler(BaseFileHandler):
    def _serialize(self, data: dict) -> str:
        return json.dumps(data)

    def _deserialize(self, data: str) -> dict:
        return json.loads(data)


student = {"name": "Вася", "group": "P33"}
txt_handler = TextFileHandler("student.txt")
txt_handler.write(student)
print(f"TXT: {txt_handler.read()}")
json_handler = JSONFileHandler("student.json")
json_handler.write(student)
print(f"JSON: {json_handler.read()}")
