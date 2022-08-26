from random import random
import random

class Bear:
  """
  Representaion of a Bear
  """
  def __init__(self, river):
    while True:
      r = random.randint(0, len(river) - 1)
      if river[r] == None:
        break
    river[r] = self   #insert instnace in river position r
    self._pos = r
    self._river = river

  def action(self, rand_action):
    curr_pos = self._pos

    if rand_action == "right":

      new_idx = curr_pos + 1
      test = self._river[new_idx]

      if test == None:
        self._pos += 1
        self._river[curr_pos] = None
        self._river[new_idx] = self
      elif isinstance(test, Fish):
        self._river[curr_pos] = None
        print(f"{type(self)} has died")
      elif isinstance(test, Bear):
        Bear(self._river)
        print("A new bear cub is born")

    if rand_action == "left":
      new_idx = curr_pos - 1
      test = self._river[new_idx]

      if test == None:
        self._pos -= 1
        self._river[curr_pos] = None
        self._river[new_idx] = self
      elif isinstance(test, Fish):
        self._river[curr_pos] = None
        print(f"Fish has Died")
      elif isinstance(test, Bear):
        Bear(self._river)
        print("A new bear is born")
    
    if rand_action == "nothing":
      pass

    def perform_action(self):
      actions = ["right", "left", "nothing"]
      rand_action = random.sample(list(actions), k=1)[0]
      print(f"{type(self)} performed {rand_action} at {self._pos}")
      result = self.consequence(rand_action)


class Fish:
  """
  Representaion of a Bear
  """

  def __init__(self, river):
    while True:
      r = random.randint(0, len(river) - 1)
      if river[r] == None:
        break
    river[r] = self  # insert instnace in river position r
    self._pos = r
    self._river = river

  def action(self, rand_action):
    curr_pos = self._pos

    if rand_action == "right":

      new_idx = curr_pos + 1
      test = self._river[new_idx]

      if test == None:
        self._pos += 1
        self._river[curr_pos] = None
        self._river[new_idx] = self
      elif isinstance(test, Fish):
        Fish(self._river)
        print("New Fish")
      elif isinstance(test, Bear):
        self._river[curr_pos] = None
        print("Fish is dead")

    if rand_action == "left":
      new_idx = curr_pos - 1
      test = self._river[new_idx]

      if test == None:
        self._pos -= 1
        self._river[curr_pos] = None
        self._river[new_idx] = self
      elif isinstance(test, Fish):
        Fish(self._river)
        print("New Fish")
      elif isinstance(test, Bear):
        self._river[curr_pos] = None
        print("Fish is dead")

    if rand_action == "nothing":
      pass

    def perform_action(self):
      actions = ["right", "left", "nothing"]
      rand_action = random.sample(list(actions), k=1)[0]
      print(f"{type(self)} performed {rand_action} at {self._pos}")
      result = self.consequence(rand_action)


class Animal:
  """Animal class"""

  def __init__(self, gender, river, strength):
    k = 0
    while True:
      r = random.randint(0, len(river) - 1)
      if not river[r]:
        break
      k += 1

      if k >= int(0.8 * len(river)):
        river += [None] * 100

    river[r] = self
    self._pos = r
    self._gender = gender
    self._river = river
    self._strength = strength

  def move(self, side):
    curr_pos = self._pos
    
    if side == "right":
      new_idx = curr_pos + 1
      self._pos = new_idx
      self._river[self._pos] = self
      self._river[curr_pos] = None
      return True

    if side == "left":
      new_idx = curr_pos - 1
      self._pos = new_idx
      self._river[self._pos] = self
      self._river[curr_pos] = None
      return True
      
    