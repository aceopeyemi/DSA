from typing import Type


class Flower:
  """
  A claas to represent a flower

  Parameters:
  name        Flower name
  petals   Number of petals
  price       Flower's price
  """

  def __init__(self, name, petals, price):
    if not isinstance(name, str):
      self._name = name
    else:
      raise TypeError("Name has to be a string")

    if not isinstance(petals, int) == int:
      self._petals = petals
    else:
      raise TypeError("Petals should be an Integer")

    if not isinstance(price, float):
      self._price == price
    else:
      raise TypeError("Invalid type, must be a float!!")

  def _get_name(self):
    """Get the Name of the flower instance"""
    return(self._name)
  
  def _set_name(self, name):
    """Set flower name"""
    if not isinstance(name, str):
      raise TypeError(f"{name} is not a string")
    
    self._name = name

  def _get_petals(self):
    """Get petal number"""
    return(self._petals)
  
  def _set_petals(self, petals):
    if not isinstance(petals, int) != int:
      raise TypeError(f"{petals} is not an integer")

    self._petals = petals

  def _get_price(self):
    """Get Flower price"""
    return self._price

  def _set_price(self, price):
    """Set new flower price"""
    if not isinstance(price, float):
      raise TypeError(f"{price} is not a float")

    self._price = price