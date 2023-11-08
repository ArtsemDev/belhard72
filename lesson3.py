# a = 5
# print(abs(a))
# print(pow(a, 2))
# print(round(3.2423, 2))
# print(divmod(5, 2))
# print(chr(65))
# print(oct(1234))
# print(hex(1234))
# print(bin(1234))
# from copy import deepcopy

# text = "hello world"
# print(text[4::2])
# print(len(text))

# a = 5
# b = 6
# result1 = "%s + %s = %s" % (a, b, a + b)
# result2 = "{} + {} = {}".format(a, b, a + b)
# result3 = f"{a} + {b} = {a+b} 🔥"
# print(result1)
# print(result2)
# print(result3)

# text = "Hello-|-world-|-python234-|-world-|-pycharm-|-belhard"
# text = text.replace("-|-", " ", 2)
# print(text)
# print(text.partition("world"))
# print(text.rpartition("world"))
# print(text.count("world"))
# print(text.find("world", 9))
# print(text.rfind("world", 9))
# words = text.split("-|-")
# result = " - ".join(words)
# print(result)
# words1 = text.split(sep="-|-", maxsplit=2)
# words2 = text.rsplit(sep="-|-", maxsplit=2)
# print(words1)
# print(words2)
# text = "Hello World"
# print(text.istitle())
# print(text.startswith("Hell"))
# print(text.endswith("rld"))
# a = "ß"
# print(a.islower())
# print(a.upper())
# print(a.title())
# print(a.capitalize())
# print(a.swapcase())
# print(a.casefold())
# print(a.lower())
# text = "Hello"
# new_text = text.upper()
# print(text)
# print(new_text)
# text = "text\tworld\tpython"
# text2 = "belhard\tpycharm\tjetbrains"
# print(text.expandtabs(tabsize=10))
# print(text2.expandtabs(tabsize=10))
# text = "-,.,.,.,-Hello---,,world,.,.,.,.,.-----,.,"
# print(text.replace(".", "").replace(",", "").replace("-", ""))
# print(text.lstrip(".,-"))
# print(text.rstrip(".,-"))
# print(text.strip(".,-"))


# text = "Hello"
# print(text.center(11, "-"))
# print(text.ljust(11, "-"))
# print(text.rjust(11, "-"))
# print(text.zfill(11))


# print(bin(13)[2:].zfill(8))

# text = "🔥".encode()
# print(len(text))


# text = "Hello\nworld".splitlines()
# print(text)

# print("hello" not in "world hello python hello")

# text1 = "hellp"
# text2 = "hello world"
# print(text1 < text2)

# print(chr(23))

# print(ord("H"), ord("E"), ord("L"), ord("L"), ord("O"))
# print(ord("H"), ord("E"), ord("l"), ord("l"), ord("o"))


# print(bin(13))
# print(bin(11))
# print(bin(6))
# print(13 ^ 11)

# print(~-12)


# text = "hello world"
# print(text[1], text[~1])

# print(bin(13))
# print(bin(13 << 2))
# print(13 >> 2)


#  Пользователь вводит текст с клавиатуры (состоящий минимум из 2х слов)
#  Используя методы поиска, с так же срезы и сложения строк, переставить первое и последнее слова
#  местами
#  пример:
#  text = "Hello python world"
#  result = "world python Hello"
# text = input("Enter text: ").strip()
# words = text.split()
# words[0], words[-1] = words[-1], words[0]
# result = " ".join(words)
# first_space_index = text.find(" ")
# last_space_index = text.rfind(" ")
# first_word = text[:first_space_index]
# last_word = text[last_space_index + 1 :]
# center = text[first_space_index : last_space_index + 1]
# result = last_word + center + first_word
# print(result)


# numbers = [6, 7, "3", 9, "fghj", 2, 6]
# text = "hello world"
# symbols = list(text)
# print(symbols)

# words = ["hello", "world", "python", "pycharm"]
# print(len(words))
# print(words + words)
# print(words[1])
# print(words[1:3])
# words[1] = 12345
# print(words)

# text = "Hello"
# words = [text, text, text]
# print(words[0] is words[1] is words[2] is text)
# objs = [
#     2,
#     3,
#     4,
#     3,
#     5,
# ]
# res = objs.copy()
# objs.sort()
# print(objs)
# print(objs.count(3))
# print(objs.index(3))
# objs.remove(3)
# a = objs.pop(1)
# print(objs)
# print(a)
# objs.extend([6, 7, 8, 9])
# print(objs)
# objs.insert(0, 10)
# print(objs)
# objs.append(6)
# print(objs)
# objs.append(objs)
# print(objs)
# del objs[1:3]
# print(objs)

# a = [1, 2, 3]
# a = a[::-1]
# print(a)

# letters = [i.upper() for i in "hello world" if i.isalpha()]
# print(letters)
# zeros_100 = [0 for _ in range(100)]
# print(zeros_100)

# a = [1, 2, 3, 4, ["hello", "wor!ld"]]
# print(a[4][1][3])

# a = [2, 3, 4]
# a[1], a[2], a[0] = a[2], a[1], 123
# print(a)
# a[1] += 5
# print(a)

# a = [3, 4, 5]
# b = [6, 7, 8]
# c = [*a, *b, *"hello"]
# print(c)


# a = [3, 4, 5, 6]
# b = a[0]
# c = a[1]
# d = a[2:]
# b, c, *d = a
# print(b)
# print(c)
# print(d)

# a = 5, 6, 7
# a[0] = 8
# print(a + a * 3)

# b = [6, 7, 8]
# a = (3, 4, 5, b)
# b.append(9)
# a[3].append(10)
# print(a)
# print(b)


# numbers = [3, 6, 2, 4, 3, 5, 12, 98]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers, start=17))
# print(reversed(numbers))
# print(sorted(deepcopy(numbers)))


# text = "Hello"
#
# letters = []
# letters.append(text)


numbers = [4, 3, 5, 4, 2, 3, 4, 7]
numbers[3:5] = "Hello"
print(numbers)
