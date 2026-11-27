experiments = [
    {"model_name": "ResNet18", "accuracy": 0.82, "loss": 0.35},
    {"model_name": "ResNet50", "accuracy": 0.88, "loss": 0.24},
    {"model_name": "EfficientNet", "accuracy": 0.91, "loss": 0.19},
    {"model_name": "MobileNet", "accuracy": 0.86, "loss": 0.32}
]
std_models = []
accuracy_table = dict()


for model in experiments:
    accuracy_table[model["model_name"]] = model["accuracy"]
    if model["accuracy"] >= 0.85 and model["loss"] < 0.3:
        std_models.append(model["model_name"])

print("Standard models: ", std_models, end=" ")       
print("\nTable of accuracy: ", accuracy_table)