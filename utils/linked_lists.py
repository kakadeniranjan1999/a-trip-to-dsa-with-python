class _Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data=None):
        self.head = _Node(data)

    def __len__(self):
        count = 0
        itr = self.head
        while True:
            if itr.next is None:
                break
            count += 1
            itr = itr.next
        return count

    def __getitem__(self, idx):
        if idx < 0:
            idx = self.__len__() + idx + 1
        count = 0
        itr = self.head
        while True:
            # if itr.next is None:
            #     break
            if count == idx:
                return itr.data
            count += 1
            itr = itr.next
        return None

    def printf(self):
        itr = self.head
        while True:
            print(f'{itr.data} ---> ', end="")
            if itr.next is None:
                break
            itr = itr.next
        print(None)

    def append(self, val):
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = _Node(val)

    def insert(self, idx, val):
        if idx < 0:
            idx = self.__len__() + idx + 1
        node = _Node(val)
        count = 0
        itr = self.head
        while True:
            if count == idx - 1:
                node.next = itr.next
                itr.next = node
                break
            count += 1
            itr = itr.next

    def pop(self, idx=-1):
        if idx < 0:
            idx = self.__len__() + idx + 1
        count = 0
        itr = self.head
        while True:
            if count == idx - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def replace(self, idx, val):
        if idx < 0:
            idx = self.__len__() + idx + 1
        count = 0
        itr = self.head
        while True:
            if count == idx:
                itr.data = val
                break
            count += 1
            itr = itr.next
