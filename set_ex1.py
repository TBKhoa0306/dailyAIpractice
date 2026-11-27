tokens = ["học", "ai", "là", "học", "cách", "xử", "lý", "dữ", "liệu", "và", "ai", "rất", "thú", "vị"]
stopwords = {"là", "và", "rất", "cách"}

# Using for loop
# cleaned_tokens = []
# for word in tokens:
#     if word not in stopwords:
#         cleaned_tokens.append(word)

# Using list comprehension
cleaned_tokens = [word for word in tokens if word not in stopwords]
print("Clean tokens: " , cleaned_tokens)

print("Vocabulary: ", sorted(list(set(cleaned_tokens))))