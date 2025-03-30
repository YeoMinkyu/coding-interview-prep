import unittest
from data_structures.arrays.dynamic_arrays import Vector

class TestVector(unittest.TestCase):
    def setUp(self):
        # Runs before each test
        self.vec = Vector()

    def test_size_initial(self):
        self.assertEqual(self.vec.size, 0)
        self.assertEqual(self.vec.capacity, len(self.vec._data))


    def test_capacity_initial(self):
        initial_size = 16

        vec = Vector(initial_size)

        self.assertEqual(vec.capacity, 2 ** (initial_size - 1).bit_length())

        initial_size = 17
        vec = Vector(initial_size)

        self.assertEqual(vec.capacity, 2 ** (initial_size - 1).bit_length())
        # self.assertEqual(vec.capacity,16) # Fail case


    def test_is_empty(self):
        self.assertTrue(self.vec.is_empty())
        self.vec.push(886)
        self.assertFalse(self.vec.is_empty())
        self.vec.pop()
        self.assertTrue(self.vec.is_empty())

    def test_at_bounds(self):
        # Test out-of-bounds access
        with self.assertRaises(IndexError):
            self.vec.at(0)  # Empty vector

        self.vec.push(10)
        self.assertEqual(self.vec.at(0), 10)

        with self.assertRaises(IndexError):
            self.vec.at(1)  # Beyond size

    def test_push_resize(self):
        for i in range(20):
            self.vec.push(i)

        self.assertEqual(self.vec.capacity, 2 ** (20 - 1).bit_length())

    def test_insert(self):
        for i in range(2):
            self.vec.push(i)

        self.assertEqual(self.vec.size, 2)
        self.vec.insert(1, 4)
        self.assertEqual(self.vec.size, 3)
        self.assertEqual(self.vec.at(0), 0)
        self.assertEqual(self.vec.at(1), 4)
        self.assertEqual(self.vec.at(2), 1)

    def test_pop_resize(self):
        for i in range(25):
            self.vec.push(i)

        for i in range(18):
            self.vec.pop()

        self.assertEqual(self.vec.capacity, 16)

    
    def test_delete(self):
        for i in range(3):
            self.vec.push(i+1)
        
        self.assertEqual(self.vec.size, 3)
        self.vec.delete(1)
        self.assertAlmostEqual(self.vec.size, 2)
        self.assertEqual(self.vec.at(1), 3)

        self.vec.delete(1)
        self.assertAlmostEqual(self.vec.size, 1)
        self.assertEqual(self.vec.at(0), 1)
        

if __name__ == '__main__':
    unittest.main()