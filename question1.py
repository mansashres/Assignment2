'''This program accepts a string and calculate the number of uppercase and lowercase'''
def count_case_letters(s):
    upper_count = sum(1 for char in s if char.isupper())  # Count uppercase letters
    lower_count = sum(1 for char in s if char.islower())  # Count lowercase letters

    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")

# Example usage
user_input = input("Enter a string: ")
count_case_letters(user_input)
