'''This program prompts the user to enter interger value.'''
# Prompt the user to enter integers for the first list
list1_input = input("Enter integers for the first list (separated by spaces): ")
list1 = list(map(int, list1_input.split()))

# Prompt the user to enter integers for the second list
list2_input = input("Enter integers for the second list (separated by spaces): ")
list2 = list(map(int, list2_input.split()))

print("\n--- Results ---")

# (a) Check if the lists are of the same length
if len(list1) == len(list2):
    print("The lists are of the same length.")
else:
    print("The lists are of different lengths.")

# (b) Check if the sums of the lists are the same
if sum(list1) == sum(list2):
    print("The sums of the lists are equal.")
else:
    print("The sums of the lists are not equal.")

# (c) Check for common elements in both lists
common = set(list1) & set(list2)
if common:
    print("The lists have common elements:", common)
else:
    print("The lists do not have any common elements.")
