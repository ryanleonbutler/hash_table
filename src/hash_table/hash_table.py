EMPTY = object()


class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.values = size * [EMPTY]

    def __len__(self) -> int:
        return len(self.values)

    def __setitem__(self, key, value):
        index = hash(key) % len(self)
        self.values[index] = value
