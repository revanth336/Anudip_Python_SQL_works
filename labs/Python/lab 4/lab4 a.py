# Input string
input_string = "P@#yn26at^&i5ve"

# Initialize count variables
char_count = 0
digit_count = 0
symbol_count = 0

# Count characters, digits, and symbols
for char in input_string:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1

# Output counts
print(f"Chars = {char_count} Digits = {digit_count} Symbol = {symbol_count}")
