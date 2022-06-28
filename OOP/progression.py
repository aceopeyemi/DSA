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


class ArithmeticProgression(Progression):
  """An Iterator producing an arithmetic progression"""

  def __init__(self, increment=1, start=0):
    """
    Create a new arithmetic progression.

    increment - Fixed constant to add to each term (default 1)
    start     - Starting point of the iteration (default 0)
    """

    super().__init__(start)
    self._increment = increment

  def _advance(self):
    """Update value by adding increment"""
    self._current += self._increment

    # return self._current


class GeometricProgression(Progression):
  """An iterator producing a geometric progession"""

  def __init__(self, base=2, start=1):
    """
      Create a new geometric progression

      base    the fixed constant multiplied to each term per iteration (default 2)
      start   the starting point of the iteration (default 0)
    """
    super().__init__(start)
    self._base = base

  def _advance(self):
    self._current *= self._base

    # return self._current

class FibonacciProgression(Progression):
  """Iterator producing a Fibonacci progression."""

  def __init__(self, first=0, second=1):
    """
    Create a new fibonacci progression.

    first     First expected value in the progression
    second    Second expected value in the progression
    """
    super().__init__(first)
    self._prev = second - first

  def _advance(self):
    """Update current value by taking sum of previous two"""
    self._prev, self._current = self._current, self._prev + self._current


# if __name__ == "__main__":
print('Default progression:' )
Progression().print_progression(10)
print('Arithmetic progression with increment 5: ')
ArithmeticProgression(5).print_progression(10)
print('Arithmetic progression with increment 5 and start 2: ')
ArithmeticProgression(5, 2).print_progression(10)
print("Geometric progression with default base: ")
GeometricProgression().print_progression(10)
print("Geometric progression with base 3: ")
GeometricProgression(3).print_progression(10)
print("Fibonacci progression with default start values: ")
FibonacciProgression().print_progression(10)
print("Fibonacci progression with start values 4 and 6: ")
FibonacciProgression(4, 6).print_progression(10)
