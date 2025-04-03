import unittest
from data_structures.queue.queue_with_fixed_arrays import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue(3)

    def test_enqueue_dequeue(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.assertEqual(self.q.dequeue(), 1)
        self.q.enqueue(3)
        self.assertEqual(self.q.dequeue(), 2)
        self.assertEqual(self.q.dequeue(), 3)

    def test_empty_full(self):
        self.assertTrue(self.q.empty())
        self.assertFalse(self.q.full())
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.assertFalse(self.q.empty())
        self.assertTrue(self.q.full())

    def test_enqueue_full(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        with self.assertRaises(ValueError):
            self.q.enqueue(4)

    def test_dequeue_empty(self):
        with self.assertRaises(ValueError):
            self.q.dequeue()


# class TestQueueWithFixedArrays(unittest.TestCase):
#     def setUp(self):
#         self.queue = Queue(5)

#     def test_enqueue(self):
#         size = 5
#         self.assertTrue(self.queue.empty())

#         for num in range(size):
#             self.queue.enqueue(num)

#         with self.assertRaises(ValueError):
#             self.queue.enqueue(5)

#         print(self.queue._queue)

#     def test_dequeue(self):
#         size = 5
#         self.assertTrue(self.queue.empty())

#         for num in range(size):
#             self.queue.enqueue(num)

#         for num in range(size):
#             self.queue.dequeue()

#         with self.assertRaises(ValueError):
#             self.queue.dequeue()
        
#         print(self.queue._queue)