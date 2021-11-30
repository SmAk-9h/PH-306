# Define function
def f(x):
    return x**4 + 2*x + 1

# Take in input for number of slices
sliceNumber = int(input("Input the number of slices you want: "))

# Set upper and lower integral bounds and set the slice size
lowerBound = 0.0
upperBound = 2.0
sliceSize = (upperBound - lowerBound) / sliceNumber

# Trapezoidal Integration
trapMethod = 0.5 * f(lowerBound) + 0.5 * f(upperBound)
for ii in range (1, sliceNumber):
    trapMethod += f(lowerBound + ii * sliceSize)
answer = round(sliceSize * trapMethod, 5)

# Print statement
print(f"For N = {sliceNumber}, the integral is {answer}")


