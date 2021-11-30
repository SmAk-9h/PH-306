# First while loop that repeats code if 1 number is not even and 1 number is not odd
isEvenOdd = 0
while isEvenOdd == 0:

# Second while loop to repeat code if both numbers input are not integers
    isInt = 0
    while isInt == 0:
        x1, x2 = input("Input one even and one odd number: ").split() # Take in 2 inputs in one line
        try:
            x1 = int(x1)
            x2 = int(x2)
            isInt = 1
        except:
            print("At least one of your inputs was not an integer")

# Determine if each value is even or odd
    if (x1 % 2) == 0:
        isEvenX1 = True
    else:
        isEvenX1 = False

    if (x2 % 2) == 0:
        isEvenX2 = True
    else:
        isEvenX2 = False

# Compare if even or odd and print out our output
    if isEvenX1 == True and isEvenX2 == False:
        isEvenOdd = 1
        print(f"{x1} is even and {x2} is odd")
    elif isEvenX1 == False and isEvenX2 == True:
        isEvenOdd = 1
        print(f"{x1} is odd and {x2} is even")
    elif isEvenX1 == True and isEvenX2 == True:
        print(f"Both {x1} and {x2} are even")
    elif isEvenX1 == False and isEvenX2 == False:
        print(f"Both {x1} and {x2} are odd")