# Define the sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries
result_dict = {**dic1, **dic2, **dic3}

# Print the concatenated dictionary
print("Expected Result:", result_dict)
