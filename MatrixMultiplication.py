# Import our libraries
import numpy as np
import time

# Take in our matrix size inputs and create the matrices
canMultiply = 0
while canMultiply == 0:   # While loop for if matrices cant be multiplied, it will ask for the inputs again
    m1Size1, m1Size2 = input('Please input the size of the first matrix (rows then columns): ').split()
    m2Size1, m2Size2 = input('Please input the size of the second matrix (rows then columns): ').split()

    if m1Size2 == m2Size1:  # This if statement makes sure that the input matrices can be multiplied
        canMultiply = 1

m1 = np.random.rand(int(m1Size1), int(m1Size2))
m2 = np.random.rand(int(m2Size1), int(m2Size2))

# Dot product multiplication
t1Start = time.time()        # Get start time of multiplication
resultant1 = np.dot(m1, m2)
t1Finish = time.time()
deltaT1 = t1Finish-t1Start   # Get end time of multiplication

print(f"The resultant matrix from the dot product multiplication is {resultant1}")
print(f"The dot product multiplication took {deltaT1} seconds")

# Manual multiplication
t2Start = time.time()        # Get start time of multiplication
resultant2Size = (int(m1Size1), int(m2Size2))
resultant2 = np.zeros(resultant2Size)

# iterating by row of matrix 1
for i in range(len(m1)):
    # iterating by column of matrix 2
    for j in range(len(m2[0])):
        # iterating by rows of matrix 2
        for k in range(len(m2)):
            resultant2[i][j] += m1[i][k] * m2[k][j]

t2Finish = time.time()       # Get end time of multiplication
deltaT2 = t2Finish-t2Start

print(f"The resultant matrix from the manual multiplication is {resultant2}")
print(f"The manual multiplication took {deltaT2} seconds")
