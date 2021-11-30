# Import exp function
from math import exp

# Take in inputs
sumNumbers = int(input('Input the total number of terms to sum: '))
KbT = float(input('Input the Kb*T value: '))

# Solve for beta
beta = 1/KbT 

# Calculate average energy
summation = 0
actualZ = 0
for ii in range(sumNumbers):
    En = ii + .05
    calcZ = exp(-beta*En)
    summation += calcZ*En
    actualZ += calcZ
avgEnergy = summation/actualZ

# Print statement
print(f"For {sumNumbers} terms and kB*T = {KbT}, the average energy is {round(avgEnergy, 5)}")