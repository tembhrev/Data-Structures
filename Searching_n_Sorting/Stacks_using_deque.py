from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')
print("Initial stack:")
print(stack)

print("Elements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Stack after elements are popped:")
print(stack)
