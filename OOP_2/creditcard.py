class CreditCard:
  """A consumer credit card"""

  def __init__(self, customer, bank, acct, limit):
    """
    Create a new credit card instance
    
    Customer - Customer name e.g(John Doe)
    Bank - Bank name e.g(GTBank)
    acct - Unique bank account identifier e.g.(5463 4567 3919 2189)
    limit - Limit set on customers credit card
    """
    self._customer = customer
    self._bank = bank
    self._acct = acct
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Return Customers name"""
    return self._customer
  
  def get_bank(self):
    """Return Bank name"""
    return self._bank

  def get_acct(self):
    """Return the unique card identifier number"""
    return self._acct

  def get_limit(self):
    """Return the limit imposed on the card"""
    return self._limit

  def get_balance(self):
    """Return the card's balance"""
    return self._balance

  def charge(self, price):
    """
    Charge given pricce to the card, provided the card is not maxed out.

    return True if processed; False if charge fails
    """

    if price + self._balance > self._limit:
      return False
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance"""
    self._balance -= amount