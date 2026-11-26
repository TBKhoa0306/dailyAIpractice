n = int(input("Input the number of elements: "))
arr = []
cnt_odd = 0
sum_of_even = 0

for i in range(n):
    arr.append(int(input(f"Input the element a[{i}]: ")))

for i in range(n):
    if arr[i] % 2 == 0:
        sum_of_even += arr[i]
    else:
        cnt_odd += 1
print("Sum of the even numbers: ", sum_of_even)
print("The number of odd numbers: ", cnt_odd)