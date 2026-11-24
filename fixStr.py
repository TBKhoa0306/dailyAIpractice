# strip() and split()
'''
- -- INPUT ---
Nhập văn bản thô: " hỌc   lẬp   trÌnH    pYtHoN cHo    AI "
- -- OUTPUT ---
Văn bản chuẩn hóa: "học lập trình python cho ai"
'''

text = input("Input string: ").strip().lower().split()

result = " ".join(text)
print(result)