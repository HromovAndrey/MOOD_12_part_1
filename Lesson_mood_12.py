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

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.data} -> {self.next}"

class DoublyLinkedList:
    def __init__(self):
       self.head = None

    def print(self):
        node = self.head
        while node is not None:
           print(node.data, end="->")
           node = node.next

    def __str__(self):
      return str(self.head)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next is not None:

            tail = tail.next

        tail.next = new_node
        new_node.prev = tail


my_list = DoublyLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)
my_list.print()




