def split_list(s, length_first_part):
    if length_first_part < 0:
        return "Invalid length of the first part"
    
    first_part = s[:length_first_part]
    second_part = s[length_first_part:]
    
    return (first_part, second_part)

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_first_part = 3

result = split_list(original_list, length_first_part)
print("Original List:", original_list)
print("Length of the first part of the list:", length_first_part)
print("Splitted the list into two parts:", result)
