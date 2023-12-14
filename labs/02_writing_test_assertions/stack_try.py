class Stack:
    def __init__(self):
        self.items = []

    def push(self, data: int) -> None:
        if not isinstance(data, int):
            raise TypeError(f"Expected int, got {type(data).__name__}")
        self.items.append(data)


# Create an instance of the Stack class
my_stack = Stack()

# This line should raise a TypeError, as "lol" is a string, not an int
my_stack.push(1)  # This should raise a TypeError
print(my_stack.items[0])