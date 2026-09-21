import unittest
from task import Check_Palindrome

class TestAssignment(unittest.TestCase):

    def test_one_deletion_palindrome(self):
        self.assertEqual(Check_Palindrome(4, 'abca'), True)

    def test_invalid_palindrome(self):
        self.assertEqual(Check_Palindrome(4, 'batr'), False)

    def test_already_palindrome(self):
        self.assertEqual(Check_Palindrome(5, 'abcba'), True)

if __name__ == "__main__":
    unittest.main()