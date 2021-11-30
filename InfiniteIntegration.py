# Import libraries
from gaussxw import gaussxwab
from math import exp, pi, sqrt, inf, log

# Create function definition and inf function definition
def f(x):
    return (sqrt(2/pi))*exp((-x**2)/2)

# Set constants
sliceNum = 50
lowerBound = 0

# Take upper bound input
upperBound = float(input('Please input the upper integration bound: '))

# Integration
answer = 0
if upperBound == inf:
    def f(z):
        return (sqrt(2/pi))*exp((-(z/(1-z))**2)/2)*(1/((1-z)**2))

    upperBoundInf = 1
    z,w = gaussxwab(sliceNum, lowerBound, upperBoundInf)
    for i in range(sliceNum):
        answer += w[i]*f(z[i])

else:
    x,w = gaussxwab(sliceNum, lowerBound, upperBound)
    for i in range(sliceNum):
        answer += w[i]*f(x[i])

roundedAns = round(answer,5)

# Output 
print(f"For upper bound = {upperBound}, the integral is {roundedAns}")
