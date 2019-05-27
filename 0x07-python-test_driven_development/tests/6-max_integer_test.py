#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
  def test_max(self):
    """Test
    """
    # Test max integer
    self.assertEqual(max_integer([1, 2, 3, 5]), 5)
    self.assertEqual(max_integer(), None)
    self.assertEqual(max_integer([1, 2, 3.5]), 3.5)
    self.assertEqual(max_integer(1, 1)
    self.assertEqual(max_integer([1, 6, 3.5]), 6)
    self.assertEqual(max_integer(["hola", "amigo"]), "hola")
    self.assertEqual(max_integer(1, 1)
    self.assertEqual(max_integer([1, 6, 3.5]), 6)
    self.assertRaises(TypeError, max_integer, [1, "hola"])
    self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
