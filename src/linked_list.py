class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        data_list = []
        node = self.head
        while node:
            data_list.append(node.data)
            node = node.next_node
        return data_list

    def get_data_by_id(self, id) -> dict:
        node = self.head
        while node:
            try:
                if node.data['id'] == id:
                    return node.data
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
            node = node.next_node

