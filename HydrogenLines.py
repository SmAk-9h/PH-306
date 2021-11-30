# Set out constants
R = .01097
m = [1,2,3]

# Calculations
for mi in m:
    n = [mi+1, mi+2, mi+3, mi+4, mi+5]
    for ni in n:
        wavelength = 1 / (R * ((1/(mi**2))-(1/(ni**2))))
        wavelength = round(wavelength, 3)   # make wavelength 
        print(f"For a m value of {mi} and a n value of {ni} the corresponding wavelength of the emission line is {wavelength} nanometers")