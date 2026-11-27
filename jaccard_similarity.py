tags_post_1 = ["python", "ai", "machine-learning", "deep-learning", "python"]
tags_post_2 = ["ai", "nlp", "python", "data-science"]

common = set(tags_post_1) & set(tags_post_2)
# print("Number of common tags: ", set(tags_post_1))
union = set(tags_post_1) | set(tags_post_2)

jaccard_similarity = float(len(common) / len(union))

print("Number of common tags: ", len(common))
print("Sum of union tags: ", len(union))
print(f"Jaccard similarity: {jaccard_similarity:.2f}")