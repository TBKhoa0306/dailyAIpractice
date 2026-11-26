weight = float(input("Nhập cân nặng: "))
height = float(input("Nhập chiều cao: "))
BMI = weight / (height * height)
print(f"Chỉ số BMI của bạn là: {BMI:.1f}")
if BMI < 18.5:
    print("Thiếu cân!")
elif BMI >= 18.5 and BMI <= 22.9:
    print("Bình thường!")
else:
    print("Béo phì!")