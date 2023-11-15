# # def is_palindrome(text):
# #     return text.lower() == text.lower()[::-1]
# #
# #
# # def foo(a, b=5):
# #     return a * b
# #
# #
# # def bar(a, b=None):
# #     if b is None:
# #         b = []
# #     b.append(a)
# #     return b
# #
# #
# # def baz(*args):
# #     print(args)
# #
# #
# # def func(**kwargs):
# #     print(kwargs)
# #
# #
# # def func2(a, b, c=33, d=None, **kwargs):
# #     print(a)
# #     print(b)
# #     print(c)
# #     print(d)
# #     print(kwargs)
# #
# #
# # def func3(*, a, b, c, d):
# #     print(a)
# #     print(b)
# #     print(c)
# #     print(d)
# #
# #
# # def func4(callback, a, b, c, d):
# #     callback(a=a, b=b, c=c, d=d)
# #
# #
# # def my_sort_func(a):
# #     return abs(int(a))
# #
# #
# # # numbers = [3, 5, "-2344", -3436, 1, 3, 2, "-567", 234]
# # # numbers.sort(key=my_sort_func)
# # # print(numbers)
# #
# #
# # # def find_max_age(user):
# # #     return user.get("age")
# #
# #
# # # [24, 34, 19, 15]
# #
# # users = [
# #     {"name": "alex", "age": 24},
# #     {"name": "pavel", "age": 34},
# #     {"name": "maria", "age": 19},
# #     {"name": "maksim", "age": 15},
# # ]
# # users.sort(key=lambda x: x.get("age"), reverse=True)
# #
# #
# # a = 5
# #
# #
# # def func5():
# #     a = 4
# #
# #     def func6():
# #         nonlocal a
# #         print(a)
# #
# #     func6()
# #     print(locals())
# #
# #
# # def my(a, b):
# #     return a + b
# #
# #
# # # numbers = ["2", "4", "2", "5", "7", "4"]
# # # numbers2 = ["a", "b", "c", "d", "e", "f"]
# # # result = map(my, numbers, numbers2)
# # # for i in result:
# # #     print(i)
# #
# #
# # # numbers = [4, 3, 4, 4, 2, 5, 6, 7, 6, 7, 6, 6, 6]
# # # result = filter(lambda x: x % 2 == 0, numbers)
# # # for i in result:
# # #     print(i)
# #
# # #
# # # names = ("Alex", "Maria", "Pavel")
# # # emails = ("alex@gmail.com", "maria@yahoo.com")
# # # #
# # # obj = zip(names, emails)
# # # data = dict(obj)
# # # print(data)
# # # for i in obj:
# # #     print(i)
# #
# # # from itertools import zip_longest
# # #
# # # obj = zip_longest(names, emails, fillvalue="Н/У")
# # # for i in obj:
# # #     print(i)
# #
# #
# # def geom_range(start, step, count):
# #     for _ in range(count):
# #         yield start
# #         start *= step
# #
# #
# # # for i in geom_range(2, 3, 50):
# # #     pass
# #
# #
# # # for j in geom_range(2, 3, 50):
# # #     print(j)
# #
# #
# # # a = geom_range(1, 2, 100)
# # #
# # # j = 0
# # # for i in a:
# # #     print(i)
# # #     j += 1
# # #     if j == 10:
# # #         break
# # #
# # #
# # # for i in a:
# # #     print(i**2)
# #
# # # with open("input.txt", "w") as file:
# # #     for _ in range(1000000000):
# # #         file.write("*" * 100 + "\n")
# #
# # # from time import sleep
# # #
# # # with open("input.txt", "r") as file:
# # #     for line in file:
# # #         print(line)
# # #         sleep(2)
# #
# #
#
#
# def foo(a):
#     text = "Hello"
#
#     def bar(b):
#         def baz(c):
#             print("bar", text, a, b, c)
#
#         return baz
#
#     return bar
#
#
# register = []
#
#
# def decorator(func):
#     register.append(func)
#
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f"{res=}"
#
#     return wrapper
#
#
# @decorator
# def multiply(*args):
#     res = 1
#     for arg in args:
#         res *= arg
#     return res
#
#
# @decorator
# def foo():
#     pass
#
#
# @decorator
# def bar():
#     pass
#
#
# # decorated_multiply = decorator(multiply)
# # print(multiply(1, 2, 3, 4, 5, 6, 7, 8))
#
#
# def args_decorator(a, b):
#     def wrapper(func):
#         def wrapped(c, d):
#             c += a
#             d += b
#             return func(c, d)
#
#         return wrapped
#
#     return wrapper
#
#
# @args_decorator(2, 3)
# def baz(x, y):
#     return x + y
#
#
#
#

#
# register = {}
#
#
# def log(method):
#     def wrapper(func):
#         def wrapped(*args, **kwargs):
#             print(method)
#             return func(*args, **kwargs)
#
#         return wrapped
#
#     return wrapper
#
#
# def dispatcher(method):
#     def wrapper(func):
#         register[method] = log(method=method)(func)
#
#         def wrapped(*args, **kwargs):
#             return func(*args, **kwargs)
#
#         return wrapped
#
#     return wrapper
#
#
# @dispatcher(method="GET")
# def hello():
#     print("HELLO")
#
#
# @dispatcher(method="POST")
# def goodbye():
#     print("GOODBYE")
#
#
# @dispatcher(method="PUT")
# def foo():
#     print("FOO")
#
#
# def error():
#     print("ERROR")
#
#
# # request = "PUT"
# # register.get(request, error)()
#
# # match request:
# #     case "GET":
# #         hello()
# #     case "POST":
# #         goodbye()
# #     case "PUT":
# #         foo()
# #     case _:
# #         error()
# # data = {"a": 1, "c": 2, "b": 3, "d": 4}
# #
# #
# # def baz(a, b, c, d):
# #     print(a, b, c, d)
# #
# #
# # baz(**data)
#
#
# numbers = [1, 2, 3, [1, 2, 3, [1, 2, 3]]]
#
#
# def recursive_multiply(numbers):
#     result = 1
#     for number in numbers:
#         if isinstance(number, (int, float)):
#             result *= number
#         else:
#             result *= recursive_multiply(number)
#     return result


# print(recursive_multiply(numbers))


#  Написать функцию factorial принимающая положительное число и возвращающая
#  факториал переданного числа


def factorial(number):
    if number == 1:
        return number
    return factorial(number - 1) * number


def is_palindrome(text: str) -> bool:
    return text.lower() == text.lower()[::-1]


def find_oldest_user(users: list[dict[str, str | int]]):
    print(users)
