# from ujson import *
from decimal import Decimal

# text = """
# {
#   "name": "Alex",
#   "age": 34,
#   "is_human": true,
#   "city": null,
#   "languages": [
#     "ru",
#     "en"
#   ]
# }
# """
#
# print(loads(text))

# with open("input.json", "r", encoding="utf-8") as file:
#     data = load(file)
# print(data)

# data = {"name": "Русские буквы", "dependencies": ["substack1", "substack2"], "arg": True}
#
# with open("out.json", "w", encoding="utf-8") as file:
#     dump(data, file, indent=2, ensure_ascii=False)
# from csv import *


# with open("out.csv", "w") as file:
#     # r = reader(file)
#     # for line in r:
#     #     print(line)
#     # r = DictReader(file, fieldnames=("name", "age", "city"))
#     # for line in r:
#     #     print(line)
#     # w = writer(file)
#     # w.writerow(["name", "age", "city"])
#     # w.writerows(
#     #     [
#     #         ["vasya", "34", "minsk"],
#     #         ["petya", "43", "mogilev"],
#     #     ]
#     # )
#     w = DictWriter(file, fieldnames=("name", "age", "city"))
#     w.writerow({"name": "Max", "age": 12, "city": "Minsk"})


# from yaml import safe_load
#
#
# with open("input.yaml", "r", encoding="utf-8") as file:
#     data = safe_load(file)
# print(data)

from re import fullmatch
from typing import *

from pydantic import (
    AfterValidator,
    BaseModel,
    EmailStr,
    model_validator,
    Field,
    FileUrl,
    validate_call,
)


def _validate_password(v: str) -> str:
    if (
        fullmatch(
            r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,64}$", v
        )
        is None
    ):
        raise ValueError
    return v


PasswordStr = Annotated[
    str,
    AfterValidator(func=_validate_password),
]


class RegisterForm(BaseModel):
    email: EmailStr
    password: PasswordStr
    confirm_password: PasswordStr

    @model_validator(mode="after")
    def password_is_match_validator(self):
        if self.password != self.confirm_password:
            raise ValueError("passwords does not match")
        return self


# class UserRegisterForm(BaseModel):
#     username: AlphaStr = Field(min_length=2)
#     email: EmailStr
#     age: int = Field(strict=True, ge=18, le=65)
#     password: PasswordStr
#     confirm_password: PasswordStr
#
#
# class LoginForm(BaseModel):
#     email: EmailStr
#     password: PasswordStr


class ProductDetail(BaseModel):
    title: str = Field(max_length=128, min_length=4)
    descr: str
    price: Decimal = Field(max_digits=10, decimal_places=2)
    image: FileUrl


class CategoryDetail(BaseModel, strict=True, frozen=True):
    name: str
    products: list[ProductDetail]
    subcategory: Optional["CategoryDetail"]


@validate_call()
def foo(a: int, b: str):
    pass
