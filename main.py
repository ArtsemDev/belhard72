print("hello github")
print("hello world")
print("python")
a = input("hello")
print(len(a))
print("another print")
name = input("Enter name: ")
print(f"{name=}")


def is_palindrome(text: str) -> bool:
    """Проверка текста на палиндром

    :param text: Текст для проверки
    :return: True - если текст является палиндромом, False - в противном случае
    """
    return text.lower() == text.lower()[::-1]
