sentence = "To change the overall look of your document. To change the look available in the gallery"
word_list = sentence.split()
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
