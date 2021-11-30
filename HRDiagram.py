# Import numpy so that we can make arrays
# Import matplotlib.pyplot so that we can make a scatter plot
import numpy as np
import matplotlib.pyplot as plt

# Import the stars.txt file
userInput = input("Input the full file name: ")
starsData = np.loadtxt(userInput)

# Split the matrix in to vectors
starsData1, starsData2 = np.hsplit(starsData,2)

# Find the length of the matrix and print it
length = np.size(starsData1)
print(f"Each array is {length} rows long")

# Find the average of each array and print them
average1 = round(np.average(starsData1),4)
average2 = round(np.average(starsData2),4)
print(f"The average of array 1 is {average1} and the average of array 2 is {average2}")

# Scatter plot
hrPlot = plt.scatter(starsData1,starsData2,s=1)
plt.xlim(15000,0)
plt.ylim(18,-5)
plt.title("Hertzsprung–Russell Diagram")
plt.xlabel("Temperature (K)")
plt.ylabel("Absolute Magnitude")
plt.show()

