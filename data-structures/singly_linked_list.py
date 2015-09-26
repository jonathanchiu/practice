class LinkedList(object):

  def __init__(self, head=None):
    self.head = head

  def insert(self, data):
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node

  def size(self):
    current_node = self.head
    size = 0
    while current_node:
      size += 1
      current_node = current_node.get_next()
    return size
    
  def search(self, data):
    current_node = self.head

    while current_node:
      if current_node.get_data() == data:
        return current_node
      current_node = current_node.get_next()

    return -1         

  def remove(self, data):
    current_node = self.head
    previous = None

    while current_node:
      at_head = current_node.get_data() == self.head.get_data()
      if current_node.get_data() == data and at_head:
        old_next = current_node.next_node
        self.head = old_next
      elif current_node.get_data() == data:
        previous.next_node = current_node.next_node

      previous = current_node
      current_node = current_node.get_next()

    return  




class Node(object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next


test = LinkedList(Node(1))
print test.head.get_data() == 1
print test.size() == 1
test.insert(5)
print test.head.get_data() == 5
print test.size() == 2
print (test.head.get_data() == 5) == True
test.insert(99)
print test.size() == 3
print (test.head.get_data() == 99) == True
print (test.search(99).get_data() == 99) == True
print (test.search(2) == -1) == True
test.insert(345)
test.insert(319)
test.insert(24)

# Current: 24 -> 319 -> 345 -> 99 -> 5 -> 1

print test.size() == 6
print test.head.get_next().get_data() == 319
test.remove(319)
print test.size() == 5
print test.head.get_data() == 24
print test.head.get_next().get_data() == 345
test.remove(1)
print test.search(5).get_next() == None

