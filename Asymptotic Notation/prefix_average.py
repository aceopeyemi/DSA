def find_max(data):
  
  """
  Return the maximum from a non empty python list
  Running Time - O(n)
  """
  biggest = data[0]

  for val in data:
    if val > biggest:
      biggest = val
  
  return biggest

arr = list(range(10, 400, 6))

max_val = find_max(arr)
print(max_val)

# Constant-Time Operations (independent of input size - O(1))
# 1. Finding the len of a python list
# 2. accessing the jth element of a list

# Linear-Time Operations (O(n))
# 1. find_max function above (randomly selected index (O(log n)))


def prefix_average1(s):
  """Return a List such that, for all j, A[j], equals average of S[0] ... S[j]"
  Quadratic Running Time"""
  n = len(s)
  A = [0] * n         # creating a new list of n zeros

  for j in range(n):
    total = 0
    for i in range(j + 1):    # computing s[1] + ... + s[j] 
      total += s[i]

    A[j] = total / (j + 1)
  
  return A


def prefix_average2(s):
  """
  Return a list such that for all j, A[j] equals average of s[0], ..., s[j]
  """
  n = len(s)
  A = [0] * n

  for i in range(n):
    A[i] = sum(s[:i + 1]) / (i + 1)


def prefix_average3(s):
  """Return list such that for all j, A[j] equals average of s[0], ..., s[j]"""

  n = len(s)
  A = [0] * n
  total = 0

  for i in range(n):
    total += s[i]
    A[i] = total / (i + 1)