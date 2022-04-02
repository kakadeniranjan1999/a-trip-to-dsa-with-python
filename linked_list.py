from utils.linked_lists import LinkedList

linked_list = LinkedList(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.printf()

print(len(linked_list))

linked_list.replace(-2, 10)
linked_list.printf()
linked_list.replace(6, 8)
linked_list.printf()
linked_list.replace(0, 12)
linked_list.printf()

print(linked_list[-4])
print(linked_list[6])
print(linked_list[-3])
print(linked_list[1])

linked_list.insert(5, 99)
linked_list.printf()

linked_list.insert(-5, 990)
linked_list.printf()

linked_list.pop(5)
linked_list.printf()

linked_list.pop(-3)
linked_list.printf()
