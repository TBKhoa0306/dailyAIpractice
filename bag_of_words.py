text = "dữ liệu là nhiên liệu mới của ai và dữ liệu quyết định sức mạnh của ai".split()
word_frequency = dict()

# Calculate the frequency of words in list 
for word in text:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print("Words frequency: ",word_frequency)

# Find the word which is the most frequency word
tmp_word = 'khoa'
tmp = -1
for key in word_frequency:
    if word_frequency[key] > tmp:
        tmp = word_frequency[key]
        tmp_word = key
print("The most frequent word: ", tmp_word, "(" , tmp, " times)")
