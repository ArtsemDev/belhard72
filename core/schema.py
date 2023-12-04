"""Schemas"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .validators import Data

from pydantic import BaseModel


__all__ = ["Schema", "User"]


class User(BaseModel):
    pass


class Schema(BaseModel):
    pass


def foo(obj: Data):
    pass
