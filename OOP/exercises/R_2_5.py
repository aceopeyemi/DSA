class CreditCard:
  """
    A customer's credit card

    The initial balance is zero

    ----------------------------
    parameters
    ----------------------------
    customer    Customer's name
    bank        The name of the bank e.g (FirstBank)
    account        The customer's credit card identifier e.g ('5391 0372 9387 5309')
    limit       Credit limit on card (measured in Naira)
  """

  def __init__(self, customer, bank, account, limit, balance=0):

    if isinstance(customer, str):
      self._customer = customer
    else:
      raise TypeError("Only Strings allowed for customer")

    if isinstance(bank, str):
      self._bank = bank
    else:
      raise TypeError("Only strings are allowed for bank")

    if isinstance(account, int):
      self._account = account
    else:
      raise TypeError("Only integers allowed for account")
    
    if isinstance(limit, (str, float)):
      self._limit = limit
    else:
      raise TypeError("Only integers or floats allowed for limit")

    if isinstance(balance, (int, float)):
      self._balance = balance
    else:
      raise TypeError("Only values of type int or float can be assigned to balance")

  def get_customer(self):
    """Returns customer's name"""
    return self._customer

  def get_bank(self):
    """Returns bank's name"""
    return self._bank
  
  def get_limit(self):
    """Return customers credit card limit"""
    return self._limit

  def get_balance(self):
    """Get Credit card balance"""
    return self._balance

  def charge(self, price):
    """
    Charge given price to the card, assuming funds are sufficient.

    Return False if charge exceeds limit; True if processed
    """

    try:
      if price + self._balance > self._limit:
        return False
      
      self._balance += price
      return True
    except TypeError as e:
      return e("Wrong typr inputted")

  def make_payment(self, amount):
    """Pay credit debt"""
    try:
      if amount < 0:
        self._balance -= amount
      else:
        raise ValueError("Amount has to be a positive integer")
    except:
      return False
