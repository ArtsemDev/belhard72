"""Модель содержащий описание объектов пользователя"""

# class User:
#     class_attr = "some value"
#
#     def foo(self):
#         self.bar()
#         self.baz()
#         print(self.class_attr)
#
#     @classmethod
#     def bar(cls):
#         print(cls.class_attr)
#         cls.baz()
#
#     @staticmethod
#     def baz():
#         print("baz")
#
#
# a = User()
# b = User()
# a.bar()
from uuid import uuid4


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.identity = uuid4()
        self.is_blocked = True
        self.age = age
        # self.i = -1

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __bool__(self):
        return self.is_blocked

    def __len__(self) -> int:
        return len(self.name)

    def __getitem__(self, item):
        return self.name[item]

    def __contains__(self, item):
        return hasattr(self, item)

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.i += 1
    #     try:
    #         return self.name[self.i]
    #     except IndexError:
    #         self.i = -1
    #         raise StopIteration

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        elif isinstance(other, int):
            return self.age == other
        else:
            raise ValueError(
                f"'==' not supported between 'Person' and '{other.__class__.__name__}'"
            )

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        elif isinstance(other, int):
            return self.age > other
        else:
            raise ValueError(
                f"'>' not supported between 'Person' and '{other.__class__.__name__}'"
            )

    def __le__(self, other):
        return not self > other

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        elif isinstance(other, int):
            return self.age < other
        else:
            raise ValueError(
                f"'<' not supported between 'Person' and '{other.__class__.__name__}'"
            )

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        if isinstance(other, Person):
            return self.age + other.age
        elif isinstance(other, int):
            return self.age + other
        else:
            raise ValueError(
                f"'+' not supported between 'Person' and '{other.__class__.__name__}'"
            )

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if isinstance(other, Person):
            self.age += other.age
            return self
        elif isinstance(other, int):
            self.age += other
            return self
        else:
            raise ValueError(
                f"'==' not supported between 'Person' and '{other.__class__.__name__}'"
            )

    def __pos__(self):
        return self.age + 1

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __isub__(self, other):
        pass


# p = Person(name="Vasya", surname="Pupkin", age=23)
# for i in p:  # type: str
#     print(i)
# p2 = Person(name="Petya", surname="Petkin", age=32)
# p += 2
# print(p.age)
# print(+p)


class Connection:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return True


# with Connection() as conn:  # type: Connection
#     print(conn.closed)
#     raise ValueError
# print(conn.closed)


# with Connection() as conn, Connection() as conn2:
#     pass


class Product:
    """Класс представления информации о товаре"""

    __slots__ = ("price", "title", "descr", "__dict__")

    def __init__(self, price, title, descr):
        self.price = price
        self.title = title
        self.descr = descr

    @classmethod
    def load(cls, data: list[dict]) -> list["Product"]:
        return [cls(**obj) for obj in data]


# product1 = Product(price=5, title="Latte", descr="HOT!")
# product1.image = "icon.png"
# print(product1.__dict__)


# m = __import__("lesson6")
# m.bar()

# import lesson6
#
#
# lesson6.bar()
