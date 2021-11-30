# Import our libraries
import numpy as np

# Define our matrices
matrixA = np.array([[-1, 2, 1],
                   [2, 3, 0],
                   [1, 0, 3]])
matrixB =np.array([[-1, 1, 3],
                  [1, 2, 0],
                  [3, 0, 2]])
matrixC = np.array([[-3, 2, 2],
                   [2, 1, 3],
                   [2, 3, 1]])

# Take in user input and figure out which matrix they selected
inputMatrix = input('Please input the capital letter of the matrix you want to calculate: ')
if inputMatrix == 'A':
    inputMatrix = matrixA
elif inputMatrix == 'B':
    inputMatrix = matrixB
elif inputMatrix == 'C':
    inputMatrix = matrixC
else:
    print("Error. Please make sure your selection is either 'A', B', or 'C'")

# Create function to calculate inverse matrix, eigenvalues, eigenvector matrix, inverse of eigenvector matrix, and diagonalization matrix
def matrixCalc(inputMatrix):
    # Make original matrix what we input
    original = inputMatrix
    
    print('')
    print('Matrix:')
    print(original)

    # Calculate inverse matrix and print it out
    inverse = np.linalg.inv(original)
    print('')
    print('Inverse matrix:')
    print(inverse)

    # Calculate eigenvalues and eigenvector and print them out
    eigenvalues, eigenvector = np.linalg.eig(original)
    print('')
    print('Eigenvalues:')
    print(eigenvalues)
    print('')
    print('Eigenvector:')
    print(np.round(eigenvector,4))

    # Calculate inverse of eigenvector
    inverseEig = np.linalg.inv(eigenvector)
    print('')
    print('Inverse of eigenvector (transpose): ')
    print(np.round(inverseEig,4))

    # Calculate diagonalization matrix
    diagonalization = np.array([[eigenvalues[0], 0, 0],
                                [0, eigenvalues[1], 0],
                                [0, 0, eigenvalues[2]]])
    print('')
    print('Diagonalization matrix:')
    print(diagonalization)



# Run the matrix calculation function
matrixCalc(inputMatrix)
