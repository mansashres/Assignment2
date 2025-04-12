'''This program create two sets.'''
# Creating the sets
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

# (a) Union of set1 and set2
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)
print("Length of the union set:", len(union_set))

# (b) Intersection of set1 and set2
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# (c) Symmetric difference (elements in either set but not both)
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference:", symmetric_difference_set)

# (d) Adding value 40 to set1
set1.add(40)  # Since 40 is already in set1, nothing changes
print("Set1 after adding 40:", set1)

# (e) Removing value 20 from set2
set2.remove(20)  # Removes 20 from set2
print("Set2 after removing 20:", set2)

