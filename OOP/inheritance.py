from classes import CreditCard

class PredatoryCreditCard(CreditCard):
  """
  A class to extend the functionality of the CrediCard class
  """

  def __init__(self, customer, bank, account, limit, apr):
    """
        initial balance is zero

        customer - customer name (e.g, 'XVIIX Bowman')
        bank - bank name (e.g, GTBank)
        account - account identifier (e.g, '5391 0378 9374 8382')
        limit - allowed credit limit (measured in dollars)
        apr - annual percentage rate (e.g, 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, account, limit)
    self._apr = apr

  def charge(self, price):
    """
    Charge given price to card, assuming sufficient credit limit

    Return True if processed
    Return False and access $5 fee if charge is denied
    """

    success = super().charge(price)     #calling inherited method
    if not success:
      self._balance += 5
    return success

  def process_month(self):
    """Assess monthly interest on outstanding balance"""
    if self._balance > 0:
      # if process balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(self._apr, 1/12)
      self._balance *= monthly_factor

class Progression:
  """
  Iterator producing a generic progression

  Default Iteration returns numbers in projection 1, 2, 3, ...
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

