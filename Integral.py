from numbers import Integral
import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np

def function(x):
	return x**3 + 2*x**2 - 4*x - 2  

def deriv(x):
	return derivative(function, x)

y = np.linspace(-6, 6, 100)

integrals = []
x_range = []
y_range = []
for i in y:
    x_range.append(i)
    y_range.append(function(i))
    integral = integrate.simps(y_range, x_range)
    integrals.append(integral)

plt.plot(y, function(y), color='purple', label='Function')
plt.plot(y, deriv(y), color='green', label='Derivative')
plt.plot(y, integrals, color='blue',label='Integral ')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
