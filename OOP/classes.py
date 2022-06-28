class CreditCard:
  """
  A customer credit card
  
  The initial balance is zero.

  customer The name of the customer e.g(John Doe)

  bank     The name of the bank e.g(GTBank)

  acct     The account identifier ('5391 0372 9387 5309')

  limit    Credit limit (measured in Naira) 
  
  """
  def __init__(self, customer, bank, account, limit):
    self._customer = customer
    self._bank = bank
    self._account = account
    self._limit = limit
    self._balance = 0
  
  def get_customer(self):
    """Return name of the customer"""
    return self._customer

  def get_bank(self):
    """Return bank's name"""
    return self._bank

  def get_limit(self):
    """Return customers credit card limit"""
    return self._limit

  def get_balance(self):
    """Return customer's credit balance"""
    return self._balance

  def charge(self, price):
    """
    Charge given price to the card, assuming sufficient credit limit.

    Return False if Charge exceeds limit; True if charge is processed
    """
    
    if price + self._balance > self._limit:
      return False
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance"""
    self._balance -= amount

if __name__ == 'main':
  wallet = []
  wallet.append(CreditCard(
    'John Bowman', 'California Savings',
    '5391 0375 9387 5309', 2500
  ))
  wallet.append(CreditCard(
    'John Bowman', "California Savings",
    '3485 0399 3395 1954', 3500
  ))
  wallet.append(CreditCard(
    'John Bowman', 'California Finance',
    '5391 0375 9387 5309', 5000
  ))

  for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2 * val)
    wallet[2].charge(3 * val)

  for c in range(3):
    print('Customer =', wallet[c].get_customer())
    print('Bank =', wallet[c].get_bank())
    print('Account =', wallet[c].get_account())
    print('Limit =', wallet[c].get_limit())
    print("Balance =", wallet[c].get_balance())
    
    while wallet[c].get_balance() > 100:
      wallet[c].make_payment(100)
      print('New balance =', wallet[c].get_balance())
    print(' ')


class Vector:
  """Represent a vector in a multidimensional space"""

  def __init__(self, d):
    """Create d-dimensional vector of zeros"""
    self._coords = [0] * d

  def __len__(self):
    """Return the dimension of the vectors"""
    return len(self._coords)
  
  def __getitem__(self, j):
    """Return jth coordinate of vector"""
    return self._coord[j]
  
  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value"""
    self._coords[j] = val

  def __add__(self, other):
    """Return sum of two vectors"""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')

    result = Vector(len(self))
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result
  
  def __eq__(self, other):
    """Return True if vector has some coordinates as other"""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other"""
    return not self == other

  def __str__(self):
    """Produces string representation of vector"""
    return '<' + str(self._coords)[1: -1] + '>'

class SequenceIterator:
  """An iterator for any of python's sequence types"""

  def __init__(self, sequence):
    """Create an iterator for the given sequence"""
    self._seq = sequence
    self._k = -1

  def __next__(self):
    """Return the next element or raise StopIteration error"""
    self._k += 1
    
    if self._k < len(self._seq):
      return(self._seq[self._k])
    else:
      raise StopIteration()

  def __iter__(self):
    """By convention, an iterator must return itself as an iterator"""
    return self


class Range:
  """A class to mimic the built-in range class"""

  def __init__(self, start, stop=None, step=1):
    """
      Initialize a range instance

      Semantics are similar to the built-in range
      function.
    """
    if step == 0:
      raise ValueError('Step cannot be 0') # check for valid step

    if stop is None:
      start, stop = 0, start

      # calculate the effective length
      self._length = max(0, (stop - start + step -1 ) // step)

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
          raise IndexError("Out of Range")  # check if index specified is within range
        
        return self._start + k * self._step

