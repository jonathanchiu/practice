import random

def quicksort(arr):
  less    = []
  greater = []
  equal   = []

  if len(arr) > 1:
    pivot = random.randint(0, len(arr) - 1)
    for n in arr:
      if n < arr[pivot]:
        less.append(n)
      elif n > arr[pivot]:
        greater.append(n)
      else:
        equal.append(n)
  else:
    return arr

  less = quicksort(less)
  greater = quicksort(greater)
  return less + equal + greater

def generate_random_array(num_elements, limit=20):
  arr = []
  for x in range(0, num_elements):
    random_number = random.randint(0, limit)
    arr.append(random_number)
  return arr

test   = generate_random_array(10, 50)
test_2 = generate_random_array(10, 50)
test_3 = generate_random_array(10, 20)

print test
print test_2
print test_3

print quicksort(test) == sorted(test)
print quicksort(test_2) == sorted(test_2)
print quicksort(test_3) == sorted(test_3)