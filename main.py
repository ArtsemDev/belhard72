def is_palindrome(text: str) -> bool:
    return text.lower() == text.lower()[::-1]


is_palindrome("1234")


class Database(object):
    data = ["value1", "value2", "value3"]

    def get(self, index):
        return self.data[index]

    def delete(self, index):
        del self.data[index]

    def add(self, value):
        if value not in self.data:
            self.data.append(value)
            return self.data.index(value)
        raise ValueError
