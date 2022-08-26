def disjoint1(A, B, C):
  """Return True if no element is common to all three lists"""
  for a in A:
    for b in B:
      for c in C:
        if a == b == c:
          return False
  return True        


def disjoint2(A, B, C):
  """Return True if no element is common to all three lists"""

  for a in A:
    for b in B:
      if a != b:          # only check C if we found no match from A and B
        for c in C:
          if a != c:
            return True
  return False