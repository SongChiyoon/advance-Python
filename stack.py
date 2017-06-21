class Stack:

    def __init__(self):
        self.stack = []  # implemented by array

    def isEmpty(self):
        return self.stack == []  # is empty

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        data = self.stack[-1]
        return data

    def sizeStack(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(3)
stack.push(5)

print("size :",stack.sizeStack())
print(stack.pop())
print("size :",stack.sizeStack())
print(stack.peek())
print("size :",stack.sizeStack())
