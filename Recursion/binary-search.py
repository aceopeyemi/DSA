def binary_search(data, target, low, high):
  """
  Return True if target is found in indicated portion of a python sequence
  
  The search only considers the portion from data[low] to data[high] inclusive

  Parameters
  ==========
  - data            - The sequence to be searched
  - target          - Target Value
  - low             - index of lowest value
  - high            - index of max value
  """

  data = sorted(data)

  if low > high:
    return False                # empty interval
  else:
    mid = (low + high) // 2

    if target == data[mid]:
      # target found

      return True
    elif target <= data[mid]:
      # perform a recursion on the left portion of the sequence

      return binary_search(data, target, low, mid -1)
    else:
      # perform a recursion on the right portion of the sequence

      return binary_search(data, target, mid + 1, high)
