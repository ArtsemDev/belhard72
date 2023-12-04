# # module = __import__("lesson10")
# # module.foo()
#
#
# # from re import compile
# #
# #
# # pattern = compile(r"[a-zA-Z]{5,}")
# #
# # text = "Hello world python pycharm"
# # print(pattern.findall(text))
# # from itertools import *
#
#
# # for i in count(1, 2):
# #     print(i)
#
#
# # text = "Hello"
# # for i in repeat(123, 5):
# #     print(i)
#
#
# # text = "ABCD"
# # text2 = "EFGH"
# # for i in product(text, text2):
# #     print(i)
#
#
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# # print(list(takewhile(lambda x: x != 4, numbers)))
# # print(list(dropwhile(lambda x: x != 4, numbers)))
#
# # print(list(compress([1, 2, 3, 4, 5], ("A", 1, 0, 1))))
# # names = ("vasya", "petya", "masha", "alex")
# # cities = ("minsk", None, None, "brest")
# # print(list(compress(names, cities)))
#
#
# # text = "Hello"
# # numbers = (1, 2, 3, 4)
# # for i in chain.from_iterable([text, numbers]):
# #     print(i)
#
#
# # text = "qwertyuiopasdfghjklzxcvbnm"
# # for i in islice(text, 0, len(text), 2):
# #     print(i)
#
# # print(tee((1, 2, 3, 4), 4))
#
# # print(list(accumulate([1, 2, 3, 4, 5, 6, 7, 8])))
#
#
# # from math import *
#
# # from pathlib import Path
# #
# #
# # BASE_DIR = Path(__file__).resolve().parent
# # path = BASE_DIR / "src/input.txt"
# #
# # with path.open(mode="r", encoding="utf-8") as file:
# #     print(file.read())
# # from datetime import *
# # from time import *
# # print(time())
# # something_date = datetime.now(tz=UTC)
# # print(something_date.strftime("%A %d %B %Y %H:%M"))
# # print(datetime.strptime("Monday 04 December 2023 17:34", "%A %d %B %Y %H:%M"))
# # datetime
# # date
# # time
# # timedelta
# # date1 = datetime(year=2015, month=3, day=4)
# # date_now = datetime.now()
# # print(date_now > date1)
# # delta = timedelta(days=5)
# # print(date_now + delta)
#
#
from dataclasses import dataclass
# # from http import HTTPStatus, HTTPMethod
#
#
@dataclass
class Response:
    status: int
    message: str
    role: int


response = Response(status=201, message="created", role=2)

#
#
# from enum import Enum, StrEnum, IntEnum
#
#
# class HTTPStatus(IntEnum):
#     OK: int = 200
#     CREATED: int = 201
#     NOT_FOUND: int = 404
#
#
# class Role(IntEnum):
#     ADMIN: int = 1
#     MANAGER: int = 2
#     USER: int = 3
#
#
# if response.role == Role.MANAGER:
#     pass

# import logging
#
#
# logging.basicConfig(
#     level=logging.INFO,
#     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
# )
# logging.info("some log")


from functools import *
from time import sleep


def decorator(func):
    """decorator docstring"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        return func(*args, **kwargs)

    return wrapper


@decorator
def foo(a: int, b: int):
    """foo docstring"""
    return a * b


# @total_ordering
# class A:
#
#     def __eq__(self, other):
#         return self == other
#
#     def __gt__(self, other):
#         return self > other

# @cache
def multiply(a, b):
    # sleep(2)
    return a * b


# numbers = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x * y, numbers))
# partial_multiply = partial(multiply, a=5)
# print(partial_multiply(b=4))
# print(partial_multiply(b=3))
# print(partial_multiply(b=2))


@singledispatch
def bar(a, b: int):
    raise TypeError


@bar.register
def _(a: int, b: int):
    return a * b


@bar.register
def _(a: str, b: int):
    return a + f"{b}"


# from argparse import ArgumentParser
#
#
# parser = ArgumentParser()
# parser.add_argument("--host", default="127.0.0.1")
# parser.add_argument("--debug", "-d", action="store_true")
# args = parser.parse_args()
# from typing import TypeVar, Any
#
#
# T = TypeVar("T")
#
#
# def bar(a: T):
#     pass
