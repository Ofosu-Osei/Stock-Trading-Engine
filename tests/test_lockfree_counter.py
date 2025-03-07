import unittest
from lockfree_counter import lib

class TestLockFreeCounter(unittest.TestCase):
    def setUp(self):
        # Create a new counter starting at 0
        self.counter = lib.create_counter(0)

    def tearDown(self):
        lib.free_counter(self.counter)

    def test_initial_value(self):
        self.assertEqual(lib.get_counter(self.counter), 0)

    def test_increment(self):
        # Increment counter and check the value
        new_val = lib.increment_counter(self.counter)
        self.assertEqual(new_val, 1)
        self.assertEqual(lib.get_counter(self.counter), 1)

    def test_multiple_increments(self):
        # Verify sequential values
        for i in range(1, 6):
            new_val = lib.increment_counter(self.counter)
            self.assertEqual(new_val, i)
        self.assertEqual(lib.get_counter(self.counter), 5)

if __name__ == '__main__':
    unittest.main()
