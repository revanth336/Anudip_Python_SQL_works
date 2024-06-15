# Input string
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Initialize count variables
upper_case_count = 0
lower_case_count = 0
numeric_count = 0
special_count = 0

# Count uppercase, lowercase, numeric, and special characters
for char in input_string:
    if char.isupper():
        upper_case_count += 1
    elif char.islower():
        lower_case_count += 1
    elif char.isdigit():
        numeric_count += 1
    else:
        special_count += 1

# Output counts
print(f"UpperCase: {upper_case_count}")
print(f"LowerCase: {lower_case_count}")
print(f"NumberCase: {numeric_count}")
print(f"SpecialCase: {special_count}")
