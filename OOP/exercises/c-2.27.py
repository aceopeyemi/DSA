class Range:
  """A class to mimic the built-in range class"""

  def __init__(self, start, stop=None, step=1):
    """
      Initialize a range instance

      Semantics are similar to the built-in range
      function.
    """
    if step == 0:
      raise ValueError('Step cannot be 0')  # check for valid step

    if stop is None:
      start, stop = 0, start

      # calculate the effective length
      self._length = max(0, (stop - start + step - 1) // step)

      # knowledge of start and step are need for __getiem__
      self._start = start
      self._step = step

      def __len__(self):
        """Returns the length of expected range"""
        return self._length

      def __getitem__(self, k):
        """Gets an item at a particular index in the range specified"""

        if k < 0:
          k += len(self)  # conerting negative indexes

        if not 0 <= k < self._length:
          # check if index specified is within range
          raise IndexError("Out of Range")

        return self._start + k * self._step

      def __contains__(self, val):
        """Checks if range contains val"""

        modulo = (val % self._step) == 0

        if ((self._start < val < self._stop) and modulo):
          return True
        elif ((self._start > val > self._stop) and modulo):
          return True
        else:
          return False
