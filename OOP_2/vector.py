class Vector:
  """Represent a vector in a multi-dimensional space"""

  def __init__(self, d):
    """Create d-dimensional vector space"""
    self._coords = [0] * d

  def __len__(self):
    """Return the dimension of the vector"""
    return len(self._coords)

  def __getitem__(self, i):
    """Return object at position i"""
    return self._coords[i]

  def __setitem__(self, i, val):
    """Set item at index i to val"""
    self._coords[i] = val

  def __add__(self, other):
    """Add vectors"""