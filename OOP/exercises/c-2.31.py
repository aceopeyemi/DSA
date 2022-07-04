class Progression:
  """
  Iterator producing a generic progression

  Default Iteration returns numbers in projection 1, 2, 3, ...

  Parameters:
  start - int, indicating the beginning of the progression
  """

  def __init__(self, start=0):
    """Initialize current to the first value of the progression."""
    self._current = start

  def _advance(self):
    """
    Update self._current to a new value on each iteration
    
    This is a protected method and can therefore be overridden in a
    subclass to customize the progression.

    Setting current to None designates the end of a finite progression

    """
    self._current += 1

  def __next__(self):
    """Return the next element in iteration or raise StopIteration error"""

    if self._current is None:
      raise StopIteration()
    else:
      answer = self._current
      self._advance()
      return answer

  def __iter__(self):
    """By convention, this method returns the class instance """
    return self

  def print_progression(self, n):
    """Print next n values in the progression"""
    print(' '.join(str(next(self)) for j in range(n)))


class ExtendProgression(Progression):
  """
  An extension of the Progression class
  """

  def __init__(self, first=2, second=200):
    """
    first - First number in progression
    second - second number in progression
    """
    self._first = first
    self._second = second
    self._prev = abs(self._second - self._first)
  
  def _advance(self):
    self._prev, self._current = self._current, abs(self._current - self._prev) 