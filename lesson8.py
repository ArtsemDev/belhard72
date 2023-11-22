# class User(object):
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password
#         self.is_active = False
#
#     def __str__(self):
#         return f"User: {self.username}"
#
#     def activate(self):
#         if not self.is_active:
#             self.is_active = True
#
#
# class Staff:
#     permissions = []
#
#
# class Manager(Staff, User):
#     def __init__(self, username, email, password, salary):
#         super().__init__(username, email, password)
#         self.salary = salary
#
#     def __str__(self):
#         data = super().__str__()
#         return data + f" {self.email}"
#
#
# # class A:
# #     def __init__(self, name):
# #         self.name = name
# #
# #
# # class B(A):
# #     def __init__(self, email):
# #         self.email = email
# #
# #
# # class C(A):
# #     pass
#
#
# # class A:
# #     pass
# #
# #
# # class B(A):
# #     pass
# #
# #
# # class C(A):
# #     pass
# #
# #
# # class D(B):
# #     pass
# #
# #
# # class E(C):
# #     pass
# #
# #
# # class F(D, E):
# #     pass
# #
# #
#
#
# # class A:
# #
# #     def __init__(self, a):
# #         self.a = a
# #
# #
# # class B(A):
# #
# #     def __init__(self, a, b):
# #         super().__init__(a)
# #         self.b = b
# #
# #
# # class C(B):
# #
# #     def __init__(self, a, b, c):
# #         super().__init__(a, b)
# #         self.c = c
#
#
# class A:
#     def __init__(self, a):
#         self.a = a
#
#     def foo(self):
#         print("A foo")
#
#
# class B:
#     def __init__(self, b):
#         self.b = b
#
#     def foo(self):
#         print("B foo")
#
#
# class C(A, B):
#     def __init__(self, a, b):
#         A.__init__(self, a)
#         B.__init__(self, b)
#
#     def foo(self):
#         print("C foo")
#
#     def info(self):
#         self.foo()
#         super().foo()
#         B.foo(self)
#
#


class A:
    attr = None

    def __init__(self, a):
        self.a = a

    def __init_subclass__(cls, **kwargs):
        # print(cls)
        # if "attr" not in kwargs:
        #     raise AttributeError

        cls.attr = kwargs.get("attr", "default value")


class B(A, attr="some value"):
    # attr = "some value"
    pass


class C(A):
    pass


class DebtCard:
    def __init__(self, card_number):
        self.__card_number = card_number

    @property
    def card_number(self):
        return self.__card_number[:6] + "******" + self.__card_number[-4:]

    @card_number.setter
    def card_number(self, value):
        if not isinstance(value, str):
            raise TypeError

        if not value.isdigit():
            raise ValueError

        self.__card_number = value


# class YandexMusic:
#     def get(self, name):
#         return name
#
#
# class Spotify:
#     def get(self, name):
#         return name
#
#
# class iTunes:
#     def get(self, name):
#         return name
#
#
# class YouTube:
#     def get(self, name):
#         return name
#
#
# yandex = YandexMusic()
# spotify = Spotify()
# itunes = iTunes()
# yt = YouTube()
#
#
# def main(obj: YandexMusic | Spotify | iTunes | YouTube, name):
#     if isinstance(obj, (YandexMusic, Spotify, iTunes, YouTube)):
#         return obj.get(name)


from abc import ABC, abstractmethod


class AbstractMedia(ABC):
    @abstractmethod
    def get(self, name: str) -> str:
        pass

    @abstractmethod
    def save(self, name) -> None:
        pass

    @classmethod
    @abstractmethod
    def download(cls):
        pass


class YandexMusic(AbstractMedia):
    @classmethod
    def download(cls):
        pass

    def get(self, name: str) -> str:
        pass

    def save(self, name) -> None:
        pass

    def upload(self):
        pass


# SOLID
# S - Single responsibility
# O - Open/Closed
# L - Liskov Substitution
# I - Interface Segregation
# D - Dependency Inversion


class AbstractPhone(ABC):
    @abstractmethod
    def call(self):
        pass


class SMSMixin:
    def sms(self, text, number):
        print(f"{text=} {number=}")


class MobilePhone(SMSMixin, AbstractPhone):
    def call(self):
        pass


class SimplePhone(AbstractPhone):
    def call(self):
        pass


class AbstractBar(ABC):
    @abstractmethod
    def get(self, **kwargs):
        pass


class Bar(AbstractBar):
    def get(self, **kwargs):
        pass


class Baz(AbstractBar):
    def __init__(self):
        self.bar = Bar()

    def get(self, **kwargs):
        return self.bar.get(**kwargs)


# def info(self):
#     return "info"
#
#
# X = type("X", (), {"__str__": info})
#
# obj = X()
# print(obj)


# class MyMeta(type):
#     def __new__(cls, clsname, superclasses, attributedict):
#         print(cls)
#         print(clsname)
#         print(superclasses)
#         attributedict["attr"] = "some value"
#         return super().__new__(cls, clsname, superclasses, attributedict)


# class Y(metaclass=MyMeta):
#     pass
#
#
# print(Y.attr)


class Singleton(type):
    _register = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._register:
            print("tut")
            cls._register[cls] = super().__call__(*args, **kwargs)
        return cls._register[cls]


class Y(metaclass=Singleton):
    def __init__(self, a):
        self.a = a
