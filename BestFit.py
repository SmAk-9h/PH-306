# Imports
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
from matplotlib import pyplot as plt

# Function Definitions
'''
This is a slope intercept function that takes in the inputs x, m (slope), and b (y intercept) and outputs the corresponding y value
'''
def func(x, m, b):
    return m * x + b

# Constants
xData = np.array([0, 2, 3, 4, 5])
yData = np.array([0, 4, 11, 14, 23.5])
yError = np.array([1, 2, 1, 1.5, 2.5])

# Run the scipy curve fit function on our data
popt, pcov = curve_fit(func, xData, yData, sigma=yError, absolute_sigma=True)
BFvalue = func(xData, *popt)   # Best Fit Y values
print(f'The a value for the line of best fit is {round(popt[1],3)}')
print(f'The b value for the line of best fit is {round(popt[0],3)}')
print(f'The covariance matrix is {pcov}')

# Create our plot
plt.plot(xData, yData, 'b-', label='Data')
plt.errorbar(xData, yData, yerr=yError, fmt='o')
plt.plot(xData, BFvalue, 'r-', label='Best Fit (Linear Model)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Find the chi squared
chi2Value = 0
for i in [0,1,2,3,4]:
    chi2Value += ((yData[i] - BFvalue[i])**2) / (yError[i]**2)

roundedChiValue = round(chi2Value, 3)
print(f'The Chi-Squared value is {roundedChiValue}')

# Determine if the fit was successful
chiCrit = round(chi2.ppf(0.9,3), 3)
print(f'The Chi-Crit value is {chiCrit}')

if roundedChiValue < chiCrit:
    print(f'Since the chi value, {roundedChiValue}, is smaller than the chi crit value, {chiCrit}, the fit was successful')
else:
    print(f'Since the chi value, {roundedChiValue}, is larger than the chi crit value, {chiCrit}, the fit was not successful')

