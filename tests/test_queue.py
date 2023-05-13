import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.head.data, 1)
        self.assertEqual(queue.tail.data, 3)
        self.assertEqual(queue.head.next_node.data, 2)
        with self.assertRaises(AttributeError):
            queue.tail.next_node.data

    def test_str(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.__str__(), "data1\ndata2\ndata3")

if __name__ == "__main__":
    unittest.main()