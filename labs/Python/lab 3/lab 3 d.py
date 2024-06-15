text = "Welcome to python Training"
vowels = "aeiouAEIOU"
vowel_count = {}
for char in text:
    if char in vowels:
        if char in vowel_count:
            vowel_count[char] += 1
        else:
            vowel_count[char] = 1
print(vowel_count)


