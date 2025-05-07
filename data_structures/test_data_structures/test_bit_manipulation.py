import unittest
from data_structures.bitwise_operation.bit_manipulation import BitManipulation

class TestBitManipulation(unittest.TestCase):
    def setUp(self):
        self.bm = BitManipulation()

    def test_min(self):
        self.assertEqual(self.bm.min(5, 3), 3)
        self.assertEqual(self.bm.min(-2, 1), -2)
        self.assertEqual(self.bm.min(0, 0), 0)

    def test_swap(self):
        self.assertEqual(self.bm.swap(5, 10), (10, 5))
        self.assertEqual(self.bm.swap(-1, -2), (-2, -1))
        self.assertEqual(self.bm.swap(3, 3), (3, 3))

    def test_absolute_value(self):
        self.assertEqual(self.bm.absolute_value(5), 5)
        self.assertEqual(self.bm.absolute_value(-5), 5)
        self.assertEqual(self.bm.absolute_value(0), 0)

    def test_count_different_bits(self):
        self.assertEqual(self.bm.count_different_bits(5, 3), 2)  # 0101 ^ 0011
        self.assertEqual(self.bm.count_different_bits(0, 0), 0)
        self.assertEqual(self.bm.count_different_bits(-1, 1), 31)

    def test_is_power_of_two(self):
        self.assertTrue(self.bm.is_power_of_two(4))
        self.assertFalse(self.bm.is_power_of_two(6))
        self.assertFalse(self.bm.is_power_of_two(0))

    def test_is_even(self):
        self.assertTrue(self.bm.is_even(4))
        self.assertFalse(self.bm.is_even(7))
        self.assertTrue(self.bm.is_even(0))
        self.assertTrue(self.bm.is_even(-2))  # Negative even number
        self.assertFalse(self.bm.is_even(-3))  # Negative odd number

    def test_is_bit_set(self):
        self.assertTrue(self.bm.is_bit_set(5, 2))   # 0101, bit 2 is 1
        self.assertFalse(self.bm.is_bit_set(5, 1))  # 0101, bit 1 is 0
        with self.assertRaises(ValueError):
            self.bm.is_bit_set(5, -1)
        with self.assertRaises(ValueError):
            self.bm.is_bit_set(5, 32)

    def test_flip_bit(self):
        self.assertEqual(self.bm.flip_bit(5, 2), 1)  # 0101 -> 0001
        self.assertEqual(self.bm.flip_bit(5, 1), 7)  # 0101 -> 0111

    def test_clear_bit(self):
        self.assertEqual(self.bm.clear_bit(5, 2), 1)  # 0101 -> 0001

    def test_set_bit(self):
        self.assertEqual(self.bm.set_bit(5, 1), 7)  # 0101 -> 0111

if __name__ == "__main__":
    unittest.main()