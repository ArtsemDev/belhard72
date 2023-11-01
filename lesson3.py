# a = 5
# print(abs(a))
# print(pow(a, 2))
# print(round(3.2423, 2))
# print(divmod(5, 2))
# print(chr(65))
# print(oct(1234))
# print(hex(1234))
# print(bin(1234))

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
