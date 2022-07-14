import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
from setting import * 

def deriv(x):
	return derivative(set.function, x)

plt.plot(y, set.function(y), color='purple', label='Function')
plt.plot(y, deriv(y), color='green', label='Derivative')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()