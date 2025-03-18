class HashTable:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.hash = data

    def __len__(self):
        count = 0
        for _ in self.hash:
            count += 1
        return count

    def _get_hash(self, key):
        sum_val = 0
        for char in key:
            sum_val += ord(char)
        print(sum_val, self.__len__() + 1, sum_val % (self.__len__() + 1))
        return sum_val % (self.__len__() + 1)

    def __getitem__(self, key):
        pass

    def printf(self):
        pass

    def append(self, key, val):
        key = self._get_hash(key)
        self.hash += [[0, 0] * key]

    def insert(self, idx, val):
        pass

    def pop(self, idx=-1):
        pass

    def replace(self, idx, val):
        pass
