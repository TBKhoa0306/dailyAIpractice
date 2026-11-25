arr = []
n = int(input("Input n: "))
for i in range(n):
    arr.append(int(input(f"Input arr[{i}]:")))

max = -1000
min = 1000

# Find max and min values
for i in range(n):
    if arr[i] > max:    
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

# Remove max and min values
while(max in arr):
    removed_maxVal = arr.remove(max)
while(min in arr):
    removed_minVal = arr.remove(min)

# Calculate average value
avg = 0
for i in range(len(arr)):
    avg += arr[i]

avg = float(avg / len(arr))

print(f"Score average: {avg:.2f}")
