from classes import CreditCard


class PredatoryCreditCard(CreditCard):
  """
  A class to extend the functionality of the CrediCard class
  """

  OVERLIMIT_FEE = 5
  CHARGE_COUNT = 0
  __slots__ = '_apr'

  def __init__(self, customer, bank, account, limit, apr, minpay, late_fees):
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
    self._minpay = minpay
    self._late_fees = late_fees

  def charge(self, price):
    """
    Charge given price to card, assuming sufficient credit limit

    Return True if processed
    Return False and access $5 fee if charge is denied
    """

    success = super().charge(price)  # calling inherited method
    if success:
        PredatoryCreditCard.CHARGE_COUNT += 1

    if not success:
      self._balance += PredatoryCreditCard.OVERLIMIT_FEE
    return success

  def process_month(self):
    """Assess monthly interest on outstanding balance"""
    fee = 1
    if PredatoryCreditCard.CHARGE_COUNT > 10:
      self._balance += fee * (PredatoryCreditCard.CHARGE_COUNT - 10)
    if self._balance > 0:
      # if process balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(self._apr, 1/12)
      self._balance *= monthly_factor
