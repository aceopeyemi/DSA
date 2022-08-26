def unique1(s):
  """Return True if no duplicates are found in s"""

  for j in range(len(s)):
    for k in range(j+1, len(s)):
      if s[j] == s[k]:
        return False
  return True


def unique2(s):
  """Return True if no duplicates are found in s"""

  n = len(s)
  s_sorted = sorted(s)

  for i in range(n):
    if s_sorted[i] == s_sorted[i + 1]:
      return False

  return True