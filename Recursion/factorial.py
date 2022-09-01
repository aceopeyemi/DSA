def factorial(n):
  """Calculate the Factorial of n (n!)"""
  
  # defining the base case
  if n == 0:
    return 1
  else:
    # recursion step
    return n * factorial(n-1)