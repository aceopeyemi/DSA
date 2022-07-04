class ReversedSequenceIterator:
  """A reverse iterator of python sequences"""

  def __init__(self, sequence):
    """Initializing iterator to reverse sequence"""
    self._seq = sequence
    self._k = 0                   # pointer to check positions

  def __next__(self):
    """Get the next element in reversed sequence"""

    self._k -= 1
    if self._k > (-1 * len(self._seq)):
      return self._seq[self._k]
    else:
      raise StopIteration()

  def __iter__(self):
    """Returns self by convention"""
    return self