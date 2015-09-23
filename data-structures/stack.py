class StackError(Exception):

  def __init__(self, error):
    self.error = error

  def __str__(self):
    return repr(self.value)

class Stack:

  def __init__(self, max_size):
    self.data = []
    self.max_size = max_size

  def push(self, e):
    if self.is_full():
      raise StackError("Can't push into a full stack")
    
    self.data.append(e)
    return self.data

  def pop(self):
    if self.is_empty():
      raise StackError("Can't pop an empty stack")

    popped = self.data[-1]
    del self.data[-1]
    return popped

  def length(self):
    return len(self.data)    

  def is_empty(self):
    return self.length() == 0

  def is_full(self):
    return self.length() == self.max_size

  def peek(self):
    temp = self.pop()
    self.push(temp)
    return temp

# Quick tests
test_stack = Stack(4)
print test_stack.is_empty() == True

test_stack.push(95)
test_stack.push(1093)

print test_stack.length() == 2
print test_stack.pop() == 1093
print test_stack.length() == 1

test_stack.push(1)
test_stack.push(2)
test_stack.push(3)

print test_stack.is_full() == True
print test_stack.peek() == 3











