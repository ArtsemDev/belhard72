# number = int(input())
# is_even = "No" if number % 2 else "Yes"

# if number % 2:
#     is_even = "No"
# else:
#     is_even = "Yes"
# print("No" if number % 2 else "Yes" if number != 0 else "Zero")

# if n := int(input()):
#     print(n)

# for i in range(1, 10):
#     i **= 2
#     print(f"{i=}")

# for _ in range(10):
#     print("Hello")

# for i in range(10):
#     if i == 10:
#         break
#     print(i)
# else:
#     print("Finish!")

# text = "Hello world"
# for i in text:
#     print(i)

# data = {"a": 1, "b": 2, "c": 3}
# for key in data:
#     print(key)

# text = "Hello"
# for i in enumerate(text):
#     print(i)

# words = ["Hello", "World", "Python"]
# for word in words:
#     for letter in word:
#         print(letter)
#
# n = int(input())
# while n > 0:
#     print(n)
#     n -= 1

# n = int(input())
# numbers = [2**i for i in range(1, n + 1) if i % 2]
# for i in range(1, n + 1):
#     if i % 2:
#         numbers.append(2 ** i)
# print(numbers)

#  Используя цикл for заполнить список квадратами 10 чисел вводимых пользователем
# numbers = []
# for _ in range(10):
#     number = int(input()) ** 2
#     numbers.append(number)

#  Переспрашивать у пользователя данные с клавиатуры до тех пор,
#  пока он не введет число

# while not (number := input("Enter number: ")).isdigit():
#     ...

#  пользователь вводит сумму вклада и процент по вкладу (вклад капитализации)
#  через сколько лет сумма вклада удвоится
#  100 под 10 = 8

# amount = float(input())
# percent = float(input())
# year = 0
# target = amount * 2
# while amount < target:
#     year += 1
#     amount *= 1 + percent / 100
# print(year)

#  Пользователь 10 раз вводит данные в следующем формате
#  Название_города население_2010 население_2020
#  Минск 1000000 1200000
#  Необходимо сформировать словарь с данные о приросте населения во введенных городах
#  {"Minsk" : 200000, ...}

# countries = {}
# for _ in range(3):
#     country_info = input().split()
#     countries[country_info[0]] = int(country_info[2]) - int(country_info[1])

#  Используя данные полученные после выполнения кода предыдущей задачи,
#  вывести название города с максимальным приростом населения

# max_population = 0
# country_name = ""
# for name, count in countries.items():
#     if count > max_population:
#         max_population = count
#         country_name = name
# print(country_name)

# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError:
#     print("invalid data")
# except ZeroDivisionError as e:
#     print("zero")
# else:
#     print("ошибок не было")
# finally:
#     print("выполняется в любом случае")


# n = input()
# if n.isdigit() and int(n) <= 0:
#     print("must be great then 0")
#
# n = int(n)

# method = "PUT"
#
# match method:
#     case "GET" | "get":
#         print("get request")
#     case "POST" | "post":
#         print("post request")
#     case _:
#         print("invalid request")


# n = ["5"]
#
# match n:
#     case int(n) | float(n):
#         print("integer")
#     case str(n):
#         print("string")
#     case _:
#         print("invalid type")

# color = ("255", 255, "0")
# if len(color) == 3:
#     r, g, b = color
# match color:
#     case r, g, b:
#         print(r, g, b)
#     case int(r), int(g), int(b), int(a):
#         print(r, g, b, a)
#     case _:
#         print("invalid")

# numbers = (23, 45, 87)
# match numbers:
#     case 23 as first, 45 as second, 87 as third:
#         print(first, second, third)

# text = ["H", "e", "l", "l", "o"]
#
#
# match text:
#     case "H" as a, "e" as b, "l" as c, "l" as d, "o" as e:
#         print(a, b, c, d, e)


# objs = [1, 2, 3, (4, 5, 6)]
#
# match objs:
#     case int(a), int(b), int(c), tuple(d):
#         match d:
#             case int(e), int(f), int(g):
#                 print(a, b, c, d, e, f, g)

# print(all([1, 2, 3, 4, "0", None]))

# print(isinstance(True, (int, float)))
# a = 34
# print(isinstance(a, int) and not isinstance(a, bool))


# BAD
# a = 34
# if bool(a) == True:
#     pass

# a = (3, 4, 5, [])
# data = {
#     a: "Value"
# }

# text = "Hello\nworld"
# for i in text:
#     if i == "\n":
#         print("Done")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in numbers:
#     numbers.append(number)


# numbers = [4, 4, 3, 4, 3, 5, 4, 5, 6, 5, 6, 6, 5, 7]
# for number in numbers[::-1]:
#     if number % 2 == 0:
#         numbers.remove(number)
# print(numbers)

# objs = [(1, 2), (3, 4, 6), (4, 5, 7, 8)]
# for i, j, *k in objs:
#     print(i, j, k)

# a, b = input(), input()
# c = 4, 5

# a = (b := input())
# print(a is b)

# Generator
# a = tuple(i**2 for i in range(1, 10))
# print(a)
# for i in a:
#     print(i)
# print(a)


