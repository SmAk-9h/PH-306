# Define the first two terms and print off term1 since we will not continue to print term1 in the while loop
term1 = 0
term2 = 1
print(term1)

# While loop that iterates through the fibonacci sequence less than 1000
while term2 <= 1000:
    print(term2)
    term3 = term1 + term2
    term1 = term2
    term2 = term3
