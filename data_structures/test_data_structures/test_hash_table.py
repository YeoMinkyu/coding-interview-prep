import unittest
from data_structures.hash_table.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        """Initialize a hash table with size 7 before each test."""
        self.ht = HashTable(7)

    # Test hash()
    def test_hash(self):
        """Test hash function returns valid indices."""
        self.assertEqual(self.ht.hash(0, 7), 0)
        self.assertEqual(self.ht.hash(7, 7), 0)
        self.assertTrue(0 <= self.ht.hash(10, 7) < 7)

    # Test add()
    def test_add_new_key(self):
        """Test adding new key-value pairs."""
        self.ht.add(1, "one")
        self.assertTrue(self.ht.exists(1))
        self.assertEqual(self.ht.get(1), "one")

    def test_add_update_key(self):
        """Test updating value for an existing key."""
        self.ht.add(1, "one")
        self.ht.add(1, "updated")
        self.assertEqual(self.ht.get(1), "updated")

    def test_add_collision(self):
        """Test adding keys that collide (linear probing)."""
        # Assuming keys 1 and 8 hash to the same index (e.g., 1 % 7 = 1, 8 % 7 = 1)
        self.ht.add(1, "one")
        self.ht.add(8, "eight")
        self.assertTrue(self.ht.exists(1))
        self.assertTrue(self.ht.exists(8))
        self.assertEqual(self.ht.get(1), "one")
        self.assertEqual(self.ht.get(8), "eight")

    def test_add_full_table(self):
        """Test adding to a nearly full table."""
        for i in range(6):  # Fill 6 of 7 slots
            self.ht.add(i, f"value{i}")
        self.ht.add(7, "value7")  # Should work
        self.assertTrue(self.ht.exists(7))
        self.assertEqual(self.ht.get(7), "value7")
        # Note: If full table raises an error, add a test for it

    # Test exists()
    def test_exists_true(self):
        """Test exists() for keys that are present."""
        self.ht.add(1, "one")
        self.ht.add(2, "two")
        self.assertTrue(self.ht.exists(1))
        self.assertTrue(self.ht.exists(2))

    def test_exists_false(self):
        """Test exists() for keys that are not present."""
        self.ht.add(1, "one")
        self.assertFalse(self.ht.exists(2))

    # Test get()
    def test_get_existing(self):
        """Test getting values for existing keys."""
        self.ht.add(1, "one")
        self.ht.add(2, "two")
        self.assertEqual(self.ht.get(1), "one")
        self.assertEqual(self.ht.get(2), "two")

    def test_get_non_existing(self):
        """Test getting a non-existing key."""
        with self.assertRaises(KeyError):
            self.ht.get(1)

    def test_get_after_collision(self):
        """Test getting values after collisions."""
        self.ht.add(1, "one")
        self.ht.add(8, "eight")  # Collides with 1
        self.assertEqual(self.ht.get(1), "one")
        self.assertEqual(self.ht.get(8), "eight")

    # Test remove()
    def test_remove_existing(self):
        """Test removing existing keys."""
        self.ht.add(1, "one")
        self.ht.add(2, "two")
        self.ht.remove(1)
        self.assertFalse(self.ht.exists(1))
        self.assertTrue(self.ht.exists(2))
        with self.assertRaises(KeyError):
            self.ht.get(1)

    def test_remove_non_existing(self):
        """Test removing a non-existing key."""
        with self.assertRaises(KeyError):
            self.ht.remove(1)

    def test_remove_collision(self):
        """Test removing a key that caused a collision."""
        self.ht.add(1, "one")
        self.ht.add(8, "eight")  # Collides with 1
        self.ht.remove(1)
        self.assertFalse(self.ht.exists(1))
        self.assertTrue(self.ht.exists(8))
        self.assertEqual(self.ht.get(8), "eight")

    def test_remove_and_readd(self):
        """Test removing a key and re-adding it."""
        self.ht.add(1, "one")
        self.ht.remove(1)
        self.ht.add(1, "new_one")
        self.assertTrue(self.ht.exists(1))
        self.assertEqual(self.ht.get(1), "new_one")

if __name__ == "__main__":
    unittest.main()