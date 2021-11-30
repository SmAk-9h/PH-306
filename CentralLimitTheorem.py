# Imports
import numpy as np   # For linear alebra and matrices
from numpy import sqrt, exp, pi, random   # Commonly used numpy options 
from matplotlib import pyplot as plt    # For making graphs

# Get our 10 variables 10,000 times
sumValues = np.zeros(10000)

for ii in range(10000):
    values10 = random.uniform(0, 2, [10,1])
    sumValues[ii-1] = np.sum(values10)

# Calculate our statistics
sigma = np.std(sumValues)
medianData = np.median(sumValues)
confInterval = [round(medianData - sigma, 2), round(medianData + sigma, 2)]

# Plot our results
count, bins, ignored = plt.hist(sumValues, 50, density=True)
mu = 10  # Mean of the data should be 10
gaussianData = 1/(sigma * sqrt(2 * pi)) * exp( - (bins - mu)**2 / (2 * sigma**2) )
plt.plot(bins, gaussianData, linewidth=2, color='r')
plt.xlabel('Sum of variables')
plt.ylabel('PDF of sum')
plt.xticks([0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20])
plt.yticks([0, .05, .1, .15, .2, .25])
plt.show()

# Output std, mean, and confidence interval
print(f'Standard Deviation: {round(sigma, 2)}')
print(f'Median: {round(medianData, 2)}')
print(f'Confidence Interval: {confInterval}')


