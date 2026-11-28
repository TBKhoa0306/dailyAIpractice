logs = [
    {"model": "BERT", "epoch": 1, "val_loss": 0.4521},
    {"model": "RoBERTa", "epoch": 1, "val_loss": 0.4105},
    {"model": "BERT", "epoch": 2, "val_loss": 0.3890},
    {"model": "RoBERTa", "epoch": 2, "val_loss": 0.3512},
    {"model": "BERT", "epoch": 3, "val_loss": 0.3950},
    {"model": "RoBERTa", "epoch": 3, "val_loss": 0.3208}
]
tmp = []
grouped_logs = dict()

# Group by model name
for log in logs:
    model_name = log["model"]
    if model_name not in grouped_logs:
        grouped_logs[model_name] = []

    tmp = grouped_logs[model_name].append(log["val_loss"])

# Calculate the average of value_loss
# WAY 1: using for loop 
# avg_loss = dict()
# avg_loss = grouped_logs.copy()
# for i in avg_loss:
#     avg_loss[i] = round(sum(avg_loss[i]) / len(avg_loss[i]) , 4)

# WAY 2: using dict comprehension
avg_loss = {
    model: round(sum(losses) / len(losses), 4)
    for model, losses in grouped_logs.items()
}
# Find the model which has a lowest value loss
min = 1000
model_name = ''
epoch_num = ''
for log in logs : 
    if log["val_loss"] < min:
        min = log["val_loss"]
        model_name = log["model"]
        epoch_num = log["epoch"]

print("Group logs: ", grouped_logs)
print("Average loss: ",avg_loss)
print(f"Best checkpoint:  {model_name} (Epoch {epoch_num}) with val_loss = {min} ")
