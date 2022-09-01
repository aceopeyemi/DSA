from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def time_complexity(n):
  """
  Plot time complexities for n

  Parameters
  ============
  n - int, list, ndarray.
      when n is an int a list is creating containing n elements.
  """
  if isinstance(n, (list, np.ndarray)):
    x =  np.log(n)
    plt.figure(figsize=(15, 10))
    plt.plot(x, 8*x, label="8n", color="red")
    plt.plot(x, 4*x(np.log(x)), label="4nlogn")
    plt.plot(x, 2*(x ** 2), label="$2n^2$")
    plt.plot(x, x ** 3, label="$n^3$")
    plt.plot(x, 2**x, label="$2^n$")

    plt.xlabel("X - log n")
    plt.ylabel("Y")
    plt.title("Time Complexities")
    plt.legend()
    plt.show()

    
