from math import sqrt
from progression import Progression

class RootProgression(Progression):
  """
  A class that extends the Progression class so that each value
  in the progression is the square root of the previous value.
  """


  def __init__(self, start=65536):
    super().__init__(start)

  def _advance(self):
    self._current = sqrt(self._current)

  