# data = {"name": "Alex", "age": 23, "lang": ["ru", "en"]}
# data2 = dict(name="pavel", age=34)
# data2 = dict([("name", "alex"), ("age", 34)])
# print(data2)
# data3 = dict.fromkeys(["name", "age"])
# print(data3)


# data = {"name": "Alex", "age": 23, "lang": ["ru", "en"]}
# print(data["city"])
# print(data["name"])
# data["name"] = "Pavel"
# data["city"] = "Minsk"
# print(data)
# print("name" in data)
# print(len(data))
# print(data.get("city", "Н/У"))
# print(data.setdefault("city", "Н/У"))
# print(data)
# del data["name"]
# print(data.pop("city", None))
# print(data)
# print(data.popitem())
# print(data)
# print(list(data))
# print(data.items())


# data = {"name": "Alex", "age": 23, "lang": ["ru", "en"]}
# new_data = {"name": "Pavel", "city": "Minsk"}
# result = {**data, **new_data}
# print(result)
# data.update([("name", "Pavel"), ("city", "Minsk")])
# print(data)
# print(data)
# result = data | new_data


# data = {4, 5, 35, 2, 5, 71, 8, 2, 4, 3, 10}
# print(data)

# data = set("hello")
# print(data | set("python") | {4, 3, 5, 4})
# result = data.union("python", (3, 4, 2, 4, 3))
# print(result)
# print(data.issuperset("oleh"))
# print(data.isdisjoint("pyt"))
# print(data.issubset("hello python"))
# print(data <= set("hello python"))
# data.remove("E")
# print(data)
# data.add(67)
# print(data)
# print(data.pop())
# print(data)
# s = frozenset("hello world")
# print(s)

# number1 = float(input())
# number2 = float(input())
# number3 = float(input())
# positive_count = (number1 > 0) + (number2 > 0) + (number3 > 0)
# negative_count = (number1 < 0) + (number2 < 0) + (number3 < 0)
# zero_count = (number1 == 0) + (number2 == 0) + (number3 == 0)


# from collections import *


# text = "Hello world"
# symbols_counter = Counter(text)
# # print(symbols_counter.most_common(n=3))
# # print(list(symbols_counter.elements()))
# print(symbols_counter)
# counter2 = Counter("hello python")
# print(counter2)
# print(symbols_counter - counter2)

# data = defaultdict(list)
# data["lang"].append("ru")
# print(data)
# data1 = {"a": 1, "b": 2}
# data2 = {"b": 3, "c": 4}
# chain = ChainMap(data1, data2)
# chain["c"] = 5


# User = namedtuple("User", ("name", "email", "age"))
#
# vasya = User(name="Vasya", email="vasya@gmail.com", age=34)
# print(vasya.email)
# print(vasya._asdict())


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# q = deque(numbers)
# print(q[1])
# q.rotate(-2)
# print(q)


# objs = [i * 3 for i in "Hello world"]
# print(objs)
# numbers = [i * 10 for i in range(1, 10, 2)]
# print(numbers)
# data = {f"name-{i}": input(f"Name {i}: ") for i in range(1, 10)}
# print(data)

# numbers = [i for i in range(10)]
# numbers = [*range(10)]
# print(numbers)
# objs = [1, 2, 3, 4]
# a, b, *c = objs

# text = "Hello"
# s = (*text,)
# print(s)

# data = {"a": 2, "b": 3}
# a = [*data.values()]
# print(*a)


# numbers = [i for i in range(2, 100, 2) if i % 4 != 0]
# print(numbers)

# text = "Hello world 2345"
# letters = [i for i in text if i.isalpha()]
# print(letters)
# a = "²"
# print(a.isdigit())
# print(a.isnumeric())
# print(a.isdecimal())

# zero_array = [[j for j in range(i)] for i in range(10)]
# print(zero_array)


#  Дано некоторое положительное число N
#  Сгенерировать словарь
#  N = 3
#  data = {
#      1: [1],
#      2: [1, 2],
#      3: [1, 2, 3]
#  }

# n = int(input())
# data = {i: [j for j in range(1, i + 1)] for i in range(1, n + 1)}
# print(data)

# data = {"name": "alex"}
# text = "Hello {name}"
# text = text.format_map(data)
# print(text)

# text = "HELLO"
# data = text.maketrans({"H": "Х", "E": "Е", "L": "Л", "O": "О"})
# print(data)
# text = text.translate(data)
# print(text)


# numbers = [i.upper() for i in input().split() if i.isalpha()]
# print(numbers)

# numbers = [int(i) for i in input().split() if i.isdigit()]
# print(numbers)


# objs = {i: j for i, j in enumerate("HELLO")}
# print(objs)
# text = "HELLO"
# objs = {i: text[i] for i in range(len(text))}
# print(objs)


# text = "HELLO"
# data = dict(enumerate(text))
# print(data)

# n = input()
#
# if n.isdigit():
#     print("digit")
# elif n.isalpha():
#     print("alpha")
# else:
#     print("some value")

# n = input()

# if n.isdigit() and int(n) > 5:
#     print("body")


# if n.isdigit() or n.isalpha() and n.isupper():
#     print("body")


# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# a = 5
# print(isinstance(a, int | float))

# print(any([4, 5, 6, 7, 8, None]))

# a = "123"
# b = 0
# c = a and b
# print(c)

# session = "custom session"
# default_session = "default"
# conn = session or default_session
# print(conn)

# if session is None:
#     conn = "default"
# else:
#     conn = session


# n = 16
# print((n & (n - 1) == 0) and n != 0)
# print(bin(16))
# print(bin(15))


# n = int(input())
# numbers = [2 ** i for i in range(1, n + 1)]


# text = input()
# letters_count = {i: text.count(i) for i in text if i.isalpha()}
# print(letters_count)

# n = int(input())
# data = {i: {"name": input(), "email": input()} for i in range(1, n + 1)}
