series = [10.0, 12.5, 11.0, 14.0, 15.5, 13.0]
window_size = 3
tmp = window_size
list_of_x = [] 
list_of_y = [] 

# Create X and Y by using for loop + slicing
# for i in range(len(series)):
#     if len(list_of_x) < tmp:
#         list_of_x.append(series[i:window_size])
#         window_size += 1
#         list_of_y.extend(series[window_size - 1 : window_size + 1 : 2])

# Create X and Y by using only slicing
num_samples = len(series) - window_size
list_of_x = [series[i : i + window_size] for i in range(num_samples)]
list_of_y = [series[i + window_size] for i in range(num_samples)]

# Packaged as a List of Dicts
dataset = [ 
    {
        "sample_id" : i,
        "features" : list_of_x[i],
        "target" : list_of_y[i],
        "mean_features" : round(sum(list_of_x[i]) / len(list_of_x) , 2)
    }
    for i in range(tmp)
]

print("X: ",list_of_x)
print("Y: ",list_of_y)
print("Dataset: ",dataset)