# Import packages needed
from math import sqrt,sin,pi
import numpy as np
import matplotlib.pyplot as plt

# Take in inputs
separation = float(input("Input the seperation of the centers of the circles in in cm: "))  # Seperation of centers in cm
side = float(input("Input the length of a side of the square in cm: "))                     # Side of square in cm
wavelength = float(input("Input the wavelength of each wave in cm: "))                      # Wavelength of waves
amplitude = float(input("Input the amplitude of each wave in cm: "))                        # Amplitude of waves

# Set our non input numbers
k = 2*pi/wavelength     # Wave vector
points = 1000           # Number of grid points along each side
spacing = side/points   #Spacing of points in cm

# Find where the centers of the two circles lie
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Make an empty array which will be used to store our output values
outputArray = np.empty([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        wave1 = sqrt((x-x1)**2+(y-y1)**2)
        wave2 = sqrt((x-x2)**2+(y-y2)**2)
        outputArray[i,j] = amplitude*sin(k*wave1) + amplitude*sin(k*wave2)

# Make and show the plot
plt.imshow(outputArray, origin="lower", extent=[0,side,0,side])
plt.gray()
plt.show()




