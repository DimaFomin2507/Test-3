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


# №2

text = """Всем привет как дела тра та та"""
pure_text = text.lower().replace('', '')
letters = {
    letter: pure_text.count(letter)
    for letter in set(pure_text)
}
print(letters)

