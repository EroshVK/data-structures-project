import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        list_ = ll.to_list()
        self.assertEqual(list_[0], {'id': 0, 'username': 'serebro'})
        self.assertEqual(list_[3], {'id': 3, 'username': 'mosh_s'})
        self.assertEqual(list_[1]['username'], 'lazzy508509')

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})

        item_data = ll.get_data_by_id(3)
        self.assertEqual(item_data, {'id': 3, 'username': 'mosh_s'})

        self.assertRaises(TypeError, LinkedList, "Данные не являются словарем или в словаре нет id.")


if __name__ == "__main__":
    unittest.main()
