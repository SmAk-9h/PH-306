# Import our needed libraries
from matplotlib import pyplot as plt
import numpy as np
from numpy import pi, exp, sqrt

# Set our constant values
mu = 100
sigma = 15
numSamples = 1000

# Randomly draw from gaussian distribution
randomData = np.random.normal(mu, sigma, numSamples)

# Sort and calculate upper and lower 5%
sortedData = np.sort(randomData)
lenSorted = len(sortedData)
lowerIndex, medianIndex, upperIndex = 49, 499, 949   # n-1 term for 50th, 500th, and 950th value (these are the 5%, median, and 95% values)
lowerValue = sortedData[lowerIndex]
medianValue = sortedData[medianIndex]
upperValue = sortedData[upperIndex]

# Plot
count, bins, ignored = plt.hist(randomData, 50, density=True)
gaussianData = 1/(sigma * sqrt(2 * np.pi)) * exp( - (bins - mu)**2 / (2 * sigma**2) )
plt.plot(bins, gaussianData, linewidth=2, color='r')
plt.show()

# Calculate errors
lowerError = abs(lowerValue - sortedData[0])
upperError = abs(upperValue - sortedData[999])

# Outputs
print(f'Length: {lenSorted}')
print(f'Lower 5%: {lowerIndex+1}')
print(f'Lower 5% value: {lowerValue}')
print(f'Upper 5%: {upperIndex+1}')
print(f'Upper 5% value: {upperValue}')
print(f'Median: {medianIndex+1}')
print(f'Median value: {medianValue}')
print(f'Lower error: {lowerError}')
print(f'Upper error: {upperError}')