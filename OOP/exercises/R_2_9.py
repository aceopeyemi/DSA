class Vector:
  """
  -----------
  Vector
  -----------


  Representing a vector in a multidimensional space
  
  ----------
  parameters
  ----------
  d   - dimension of vector to be created (optional)

  arr - iterable represetation of vector to be created (optional)

  Vector can only accept one of the parameters not both at once.

  """

  def __init__(self, d=None, arr=None):
    """Create a d-dimensional vector of zeros"""
    if ((d is not None) and (arr is None)):
      try:
        self._coords = [0] * d
      except:
        TypeError("D must be an integer")
    elif ((arr is not None and (d is None))):
      try:
        self._coords = arr
      except:
        TypeError("arr must be an iterable type")
    else:
      ValueError("Vector cannot accept both parameters")

  def __len__(self):
    """Returns the length of vector instance"""
    return len(self._coords)

  def __getitem__(self, j):
    """Returns the element of vector at position j"""
    return self.coords[j]
  
  def __setitem__(self, j, val):
    """Sets vector element at position j to val"""
    self._coords[j] = val

  def __add__(self, other):
    """Adds vector instance to other vector represented by other"""
    if len(self._coords) != len(other):
      raise ValueError('Dimensions must be equal')
    
    result = Vector(len(self))
    for j in range(len(self)):
      result[j] = self._coords[j] + other[j]
    return result
  
  def __sub__(self, other):
    """
      Subtracts two vectors

      Returns a new vector instance representing the difference
      between two vectors
    """
    if len(self._coords) != len(other):
      raise ValueError("Vectors must be of the same dimension")

    result = Vector(len(self))
    for i in range(len(self)):
      result[i] = self._coords[i] - other[i]

    return result

  def __eq__(self, other):
    """Return True if vector has same coordinates as other"""
    return self._coords == other._coords

  def __neq__(self, other):
    """Return True if vector differs from other"""
    result = Vector(len(self))

    for j in result:
      result[j] = -1 * self[j]
    
    return result

  def __str__(self):
    """Produces string representation of vectors"""
    return f"<{str(self._coords)[1: -1]}>"

  def __mul__(self, val):
    """
    Returns a new vector which is a result of multiplying
    the vector instance by val.
    """
    result = Vector(len(self))
    sum = 0
    if isinstance(val, (int, float)):
      for i in range(len(result)):
        result[i] = self[i] * val
        sum += result[i]

    elif isinstance(val, Vector):
      for i in range(len(result)):
        result[i] = self[i] * val[i]

    return sum

  def __rmul__(self, val):
    """
    Returns a new vector which is a result of right multiplying
    the vector by val
    """

    result = Vector(len(self))

    if isinstance(val, (int, float)):
      for i in range(len(result)):
        result[i] = val * self[i]
      
      return result