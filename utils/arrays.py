class Array:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array

    def __len__(self):
        count = 0
        for _ in self.array:
            count += 1
        return count

    def __getitem__(self, idx):
        return self.array[idx]

    def printf(self):
        print(f'{[i for i in self.array]}')

    def append(self, val):
        self.array = self.array + [val]

    def insert(self, idx, val):
        self.append(self.__getitem__(-1))
        if idx < 0:
            idx = self.__len__() + idx
        for i in range(self.__len__() - 2, idx - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[idx] = val

    def pop(self, idx=-1):
        if idx < 0:
            idx = self.__len__() + idx
        for i in range(idx, self.__len__() - 1):
            self.array[i] = self.array[i + 1]
        self.array = self.array[:-1]

    def replace(self, idx, val):
        self.array[idx] = val
