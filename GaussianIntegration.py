# Import the gaussxw module
from gaussxw import gaussxwab

# Function definition
def f(x):
        return x**4 + 2*x + 1

# Take in # of slices from the user
sliceNum = int(input("Input the number of slices you would like to use: "))

# Integration
lowerBound = 0
upperBound = 2
x,w = gaussxwab(sliceNum, lowerBound, upperBound)
answer = 0.0
for i in range(sliceNum):
        answer += w[i]*f(x[i])
roundedAns = round(answer,5)

# Output 
print(f"For N = {sliceNum}, the integral is {roundedAns}")

