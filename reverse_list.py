arr = []
n = int(input("Input n: "))
for i in range(n):
    arr.append(int(input(f"Input arr[{i}]: ")))

print("Initial array:" , arr)

# Reverse List
reversed_list = arr[::-1]
print("Reversed List:", reversed_list)

#Output the elements at even indices
print("The elements at even indices: " , end ="") 

even_elements = reversed_list[0:len(reversed_list):2]
print(even_elements)