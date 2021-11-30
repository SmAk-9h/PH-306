# Import our needed packages
import math   # For the needed trig functions

# Take in our inputs
r = float(input("Input the r: "))
theta = float(input("Input the theta value in degrees: "))

# Convert our theta to radians
theta = math.pi / 180 * theta

# Convert to cartesian coordinates
x = round(r * math.cos(theta),3)
y = round(r * math.sin(theta),3)

# print out our cartesian coordinates
print(f"The ordered pair in cartesian coordinates is ({x},{y}) for the given r and theta values")