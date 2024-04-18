# Завдання 1
# Користувач вводить з клавіатури набір чисел. Збережіть отримані числа до однозв’язного списку. Після
# чого покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def delete_element(self, value):
        if not self.head:
            print("Список порожній")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print("Елемент не знайдено")

    def display_list(self):
        if not self.head:
            print("Список порожній")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
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
    linked_list = LinkedList()

    while True:
        display_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            data = input("Введіть число для додавання: ")
            linked_list.add_element(data)
        elif choice == "2":
            data = input("Введіть число для видалення: ")
            linked_list.delete_element(data)
        elif choice == "3":
            print("Вміст списку:")
            linked_list.display_list()
        elif choice == "4":
            data = input("Введіть число для перевірки: ")
            if linked_list.check_value(data):
                print("Число знайдено у списку")
            else:
                print("Число не знайдено у списку")
        elif choice == "5":
            old_value = input("Введіть старе значення: ")
            new_value = input("Введіть нове значення: ")
            linked_list.replace_value(old_value, new_value)
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невідома опція. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
