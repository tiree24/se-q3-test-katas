import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(10, 5), 15)
        self.assertEqual(katas.add(-1, 1), 0)
        self.assertEqual(katas.add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(katas.multiply(10, 5), 50)

    def test_power(self):
        self.assertEqual(katas.power(3, 2), 9)
        self.assertEqual(katas.power(6, 2), 36)
        self.assertEqual(katas.power(2, 4), 16)

    def test_factorial(self):
        self.assertEqual(katas.factorial(3), 6)
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(11), 39916800)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(3), 2)
        self.assertEqual(katas.fibonacci(6), 8)
        self.assertEqual(katas.fibonacci(15), 610)


if __name__ == '__main__':
    unittest.main()
