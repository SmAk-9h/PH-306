# Set our constants and take in our inputs
g = 9.8   # Gravity in m/s
TimeFlight = float(input("Please enter the time of flight in seconds: "))
InitialHeight = float(input("Please enter the initial height of the ball in meters: "))

# Solve for how far ball has fallen
deltaX = 1/2*g*TimeFlight**2
if deltaX >= InitialHeight:
    deltaX = InitialHeight

# Print how far the ball has fallen
print(f"The ball has fallen {deltaX} meters from its initial height {InitialHeight} meters in {TimeFlight} seconds")