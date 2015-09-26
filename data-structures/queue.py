class QueueError(Exception):

  def __init__(self, error):
    self.error = error

  def __str__(self):
    return repr(self.value)

class Queue:

  def __init__(self, max_size):
    self.data = []
    self.max_size = max_size

  def enqueue(self, e):
    if self.is_full():
      raise QueueError("Can't enqueue to a full queue")

    self.data.append(e)
    return self.data

  def dequeue(self):
    if self.is_empty():
      raise QueueError("Can't dequeue from an empty queue")

    dequeued = self.data[0]
    del self.data[0]
    return dequeued

  def is_empty(self):
    return len(self.data) == 0

  def is_full(self):
    return len(self.data) == self.max_size

  def peek(self):
    if self.is_empty():
      raise QueueError("Can't peek at an element of an empty queue")
    else:
      return self.data[0]


test = Queue(5)
print test.is_empty() == True
test.enqueue(6)
test.enqueue(99)
print test.peek() == 6
print test.dequeue() == 6
print test.dequeue() == 99
test.enqueue(812)
test.enqueue(82)
test.enqueue(38)
test.enqueue(91)
print test.is_full() == False
test.enqueue(999)
print test.is_full() == True


