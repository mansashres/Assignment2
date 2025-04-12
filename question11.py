'''This program 	Create three dictionaries'''
# (a) Concatenating three dictionaries into one
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

nums = {**dic1, **dic2, **dic3}  # Merge all dictionaries
print("Concatenated dictionary:", nums)

# (b) Adding a new key/value pair (7, 70)
nums[7] = 70
print("After adding (7,70):", nums)

# (c) Updating the value of key 3 to 80
nums[3] = 80
print("After updating key 3 to 80:", nums)

# (d) Removing the third item (key 3)
nums.pop(3)
print("After removing key 3:", nums)

# (e) Summing all values in nums
sum_values = sum(nums.values())
print("Sum of all values:", sum_values)

# (f) Multiplying all values in nums
product = 1
for value in nums.values():
    product *= value
print("Product of all values:", product)

# (g) Retrieving the maximum and minimum values in nums
max_value = max(nums.values())
min_value = min(nums.values())

print("Maximum value:", max_value)
print("Minimum value:", min_value)

