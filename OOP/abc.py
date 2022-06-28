from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
  """Our own Version of collections.Sequence abstract base class"""

  @abstractmethod
  def __len__(self):
    """Return the length of the sequence"""

  @abstractmethod
  def __getitem__(self, j):
    """Return element at jth index of the sequence"""

  def __contains__(self, val):
    """Return True if val found in the sequence; False otherwise"""

    for i in range(len(self)):
      if self[i] == val:
        return True
      return False

  def index(self, val):
    """Return the leftmost index at which the value is found or raise ValueError"""
    for i in range(len(self)):
      if self[i] == val:
        return i
      raise ValueError('Value not found in sequences') # if not found

  def count(self, val):
    """Return the number of elements equal to given value"""
    k = 0
    for i in range(len(self)):
      if self[i] == val:
        k += 1
    return k