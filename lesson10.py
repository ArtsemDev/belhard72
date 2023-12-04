class DictReader:

    def __init__(
            self,
            file_path: str,
            separator: str = ","
    ) -> None:
        self.file_path = file_path
        self.separator = separator
        self.file = open(file=self.file_path, mode="r")
        self.keys = self.file.readline().strip().split(self.separator)

    def __iter__(self):
        return self

    def __next__(self):
        data = self.file.readline()
        if data:
            data = data.strip().split(self.separator)
            return dict(zip(self.keys, data, strict=True))
        raise StopIteration


def foo():
    print("Foo")

if __name__ == '__main__':
    print("action")
