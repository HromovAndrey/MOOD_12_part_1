# class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #
# #     def __str__(self):
# #         return f"{self.data} -> {self.next}"
# #
# #
# # node1 = Node(12)
# # node2 = Node(99)
# # node3 = Node(37)
# #
# # node1.next = node2
# # node2.next = node3
# #
# # print(node1)
# # print(node2)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return f"{self.data} -> {self.next}"
#
# class LinkedList:
#     def __init__(self):
#        self.head = None
#
#     def __str__(self):
#         return str(self.head)
#
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         tail = self.head
#         while tail.next is not None:
#          tail.next = new_node
#
#
#         tail.next = new_node
#         print(tail)
#
#
# my_list = LinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# print(my_list)
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
#     def __str__(self):
#         return f"{self.data} -> {self.next}"
#
# class DoublyLinkedList:
#     def __init__(self):
#        self.head = None
#
#     def print(self):
#         node = self.head
#         while node is not None:
#            print(node.data, end="->")
#            node = node.next
#
#     def __str__(self):
#       return str(self.head)
#
#     def append(self, data):
#         new_node = Node(data)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         tail = self.head
#         while tail.next is not None:
#
#             tail = tail.next
#
#         tail.next = new_node
#         new_node.prev = tail
#
#
# my_list = DoublyLinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print(my_list)
# my_list.print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class RegistrationQueue:# щдно звязний список
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def move_forward(self, data):
        #Знайти node з потрібним data
        node = self.head
        while node is not None and node.data != data:
            node = node.next


        if node is None:
            print("Немає пасажира у черзі")
            return

        # переміщення в перед
        red = node.prev
        green =node
        blue =node.next
        black = node.next.next

        #змінюємо посилання в перд
        red.next, green.next, blue.next, black.next = blue, black, green

        # змінюємо посилання  на зад
         green.next, blue.prev, black.prev = blue, red, green


    def print(self):
        node = self.head

        while node is not None:
             print(node.data, and="->")
             node = node.next


my_list = BoardingQueue()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.print()
my_list.move_forvard(3)
my_list.print()
class BoaringQueue:
    pass





