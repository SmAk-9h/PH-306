# Import our needed libraries
from matplotlib import pyplot as plt
import numpy as np
from numpy import fft, sin, pi, exp, cos

# Declare our constants
N = 2000          # 2000 sample points
frequency = 4000  # 4000 Hz
T = 1/frequency  
t = np.linspace(0.0, N*T, N, endpoint=True)

# Declare function
myFunc = sin(40*2*pi*t) + .5*sin(80*2*pi*t)

# Question 1
plt.plot(myFunc)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

# Question 2 Math 
fftMyFunc = fft.fft(myFunc)
fftFreq = fft.fftfreq(N, T)[:N//2]

# Question 2 Outputs
print(f'The sampling time is {N*T} seconds')
print(f'The sampling frequency is {frequency} hertz')
print(f'The length of sampling frequency array is {len(t)}')
print(f'The length of the amplitude value array is {len(fftMyFunc)}')

# Question 2 Graphs
plt.bar(fftFreq, 1.0/N * np.abs(fftMyFunc[0:N//2]))
plt.xlim([0,100])
plt.ylim([0,1])
plt.xlabel('Frequncy (Hz)')
plt.ylabel('Amplitude')
plt.show()

# Create a function to filter the data
def filterFunc(function, value):
    # function = the function you want to filter
    # value = the minimum value of the points you want to filter
    filteredFunc = np.zeros(len(function))
    for point in range(len(function)):
        if function[point] >= value:
            filteredFunc[point] += (function[point-1] + function[point+1]) / 2
        else:
            filteredFunc[point] += function[point]
    return filteredFunc

# Run the filter function
filteredFunc = filterFunc(fftMyFunc, .4)    

# Question 3 Outputs
for ii in range(25):
    print(f'The iteration number is {ii}')
    print(f'The unfiltered fft frequency for this iteration is {fftFreq[ii]}')
    print(f'The amplitude of the fft is {round(fftMyFunc[ii], 5)}')

# Question 4
testFilteredFunc = .5*sin(80*2*pi*t)    
inverseIRFFTFiltered = fft.irfft(filteredFunc)
plt.plot(t,testFilteredFunc)   
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (after fft filtering)')
plt.show()



