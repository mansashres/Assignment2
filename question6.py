'''This program prompts the user for a series of integers '''
# Initialize an empty list to store valid numbers
valid_numbers = []

# Ask the user how many numbers they want to enter
n = int(input("How many numbers do you want to enter? "))

# Loop to take inputs from the user
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    
    # Check if the number is within the range 1-100
    if 1 <= num <= 100:
        valid_numbers.append(num)
    else:
        print("Number out of range! Only numbers between 1 and 100 are allowed.")


print("Valid numbers within range (1-100):", valid_numbers)
