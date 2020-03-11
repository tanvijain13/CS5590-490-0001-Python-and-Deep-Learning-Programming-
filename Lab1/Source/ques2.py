
# Create first dictionary
dict1 = {'Dhairya': 6, 'Tanvi': 22, 'John': 10}

# Create second dictionary
dict2 = {'Raju': 8, 'Bill': 20, 'Mark': 11}

# Concatenating two dictionaries
dict1.update(dict2)

# Printing the concatenated dictionary
print('Concatenated dictionary :', dict1)

# Sorting dictionaries by values
sortdict = sorted(dict1.items(), key=lambda x: x[1])

# Printing the sorted dictionary
print('Sorted dictionary :', sortdict)

