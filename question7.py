'''The program prompts the user to enter names separated by spaces.'''
names = input("Enter a list of names separated by spaces: ").split()

# Initialize a variable to count occurrences of the letter 'a'
count_a = 0

# Loop through each name in the list
for name in names:
    # Count how many 'a' characters are in each name (case-insensitive)
    count_a += name.lower().count('a')

print(f"The letter 'a' appears {count_a} times in the list of names.")