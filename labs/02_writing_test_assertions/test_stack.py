from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        self.stack.push(10)
        self.assertEqual(self.stack.peek(),10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(),20)

    def test_pop(self):
        """Test popping an item of off the stack"""
        self.stack.push(5)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(),3)
        self.assertEqual(self.stack.peek(),5)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        """Test peeking at the top the stack"""
        self.stack.push(5)
        self.assertTrue(isinstance(self.stack.items[0], int))
        self.stack.push(3)
        self.assertEqual(self.stack.peek(),3)


    def test_is_empty(self):
        """Test if the stack is empty"""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())


