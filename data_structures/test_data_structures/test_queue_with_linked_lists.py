import unittest
from data_structures.queue.queue_with_linked_lists import Queue


class TestQueueWithLinkedLists(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_size_empty(self):
        self.assertTrue(self.queue.empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.empty())

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.head, self.queue.tail)
        self.assertFalse(self.queue.empty())
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        print(self.queue)

    def test_dequeue(self):
        size = 10

        for num in range(size):
            self.queue.enqueue(num+1)

        print(self.queue)

        for _ in range(size):
            self.queue.dequeue()
        
        self.assertTrue(self.queue.empty())
        print(self.queue)