corpus = [
    "   Học   AI   là   tương   lai   ",
    "  Python   và   dữ   liệu   rất   quan   trọng  ",
    "  Dữ   liệu   lớn   thúc   đẩy   AI  "
]
stopwords = {"là", "và", "rất"}
test_sentence = "Python thúc đẩy công nghệ AI"

tokens = []
tmp = [] 
for word in range(len(corpus)):
    corpus[word] = corpus[word].strip().lower().split()
    tmp = tokens.extend(corpus[word])

# Filtered words through stopwords[]
clean_tokens = [word for word in tokens if word not in stopwords]

word_to_idx = dict()

union = sorted(list(set(clean_tokens)))

word_to_idx = {
    "<PAD>" : 0,
    "<UNK>" : 1
}

# WAY 1: using for loop to add new tuple into a dict
# cnt = 1  
# for word in union:
#     if word not in word_to_idx:
#         word_to_idx[word] = 1
#         word_to_idx[word] += cnt
#         cnt += 1

# WAY 2: using dict.update() + dict comprehension + enumerate()
word_to_idx.update({idx : word for word , idx in enumerate(union, start = 2)})
print(word_to_idx)
# Reversing the origin dict
reverse_dict = dict()
reverse_dict = {value : key for key, value in word_to_idx.items()}

test_sentence = test_sentence.strip().lower().split()

# WAY 1: using for loop to encode test_sentence
# encoded_test_sentence = []
# temp = []
# for word in test_sentence:
#     if word in word_to_idx:
#         temp = encoded_test_sentence.append(word_to_idx[word])
#     else:
#         temp = encoded_test_sentence.append(word_to_idx["<UNK>"])

# WAY 2: using dict comprehension
encoded_test_sentence = {
    word: word_to_idx.get(word, word_to_idx["<UNK>"]) 
    for word in test_sentence
}

print("Word_to_index: ", word_to_idx)
print("Index_to_word: ", reverse_dict)
print("Encoded test_sentence: ", encoded_test_sentence)
