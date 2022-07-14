import imp
from numbers import Integral
from typing import Set
import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np
from setting import * 

integrals = []
x_range = []
y_range = []
for i in y:
    x_range.append(i)
    y_range.append(function(i))
    integral = integrate.simps(y_range, x_range)
    integrals.append(integral)

plt.plot(y, function(y), color='purple', label='Function')
plt.plot(y, integrals, color='blue',label='Integral ')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
