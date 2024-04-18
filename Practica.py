# Завдання 2
# Користувач вводить з клавіатури набір рядків. Збережіть отримані рядки до двозв’язного списку. Після чого
# покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# Практичне завдання
# 1
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_element(self, value):
        if not self.head:
            print("Список порожній")
            return
        if self.head.data == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        while current:
            if current.data == value:
                if current.next:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    current.prev.next = None
                return
            current = current.next
        print("Елемент не знайдено")

    def display_list(self):
        if not self.head:
            print("Список порожній")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def check_value(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def replace_value(self, old_value, new_value):
        if not self.head:
            print("Список порожній")
            return
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next
        print("Елемент не знайдено")

def display_menu():
    print("Меню:")
    print("1. Додати елемент до списку")
    print("2. Видалити елемент зі списку")
    print("3. Показати вміст списку")
    print("4. Перевірити, чи є значення у списку")
    print("5. Замінити значення у списку")
    print("6. Вийти")

def main():
    doubly_linked_list = DoublyLinkedList()

    while True:
        display_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            data = input("Введіть рядок для додавання: ")
            doubly_linked_list.add_element(data)
        elif choice == "2":
            data = input("Введіть рядок для видалення: ")
            doubly_linked_list.delete_element(data)
        elif choice == "3":
            print("Вміст списку:")
            doubly_linked_list.display_list()
        elif choice == "4":
            data = input("Введіть рядок для перевірки: ")
            if doubly_linked_list.check_value(data):
                print("Рядок знайдено у списку")
            else:
                print("Рядок не знайдено у списку")
        elif choice == "5":
            old_value = input("Введіть старий рядок: ")
            new_value = input("Введіть новий рядок: ")
            doubly_linked_list.replace_value(old_value, new_value)
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невідома опція. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
