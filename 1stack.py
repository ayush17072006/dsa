class Stack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        self.stack.append(book)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Returned book:", self.stack.pop())

    def display(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Books in stack:")
            for book in reversed(self.stack):
                print(book)


s = Stack()

s.push("Python")
s.push("Data Structures")
s.push("Computer Networks")

s.display()

s.pop()
s.display()
