data = [12.5, 99.9, 13.0, 12.8, 1.2, 13.2]
# sort the origin list 
data = sorted(data)

# remove highest and lowest element
remain_ele = data[1:-1]

# calculate average value
avg = 0
for i in range(len(remain_ele)):
    avg += remain_ele[i]

print("Filtered list: ", remain_ele)
print(f"The average value: {avg / len(remain_ele):.2f}")