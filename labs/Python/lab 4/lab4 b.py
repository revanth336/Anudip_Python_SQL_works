# Input string
input_string = "String and String Function"

# Remove duplicates
output_string = ''.join(sorted(set(input_string), key=input_string.index))

# Output without duplicates
print(output_string)
