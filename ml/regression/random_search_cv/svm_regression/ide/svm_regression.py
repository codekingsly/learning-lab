from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
from itertools import product
import pandas as pd
from tabulate import tabulate

def generate_parameter_combinations(param_dict):  
    return [dict(zip(param_dict.keys(), combo)) 
            for combo in product(*param_dict.values())]

param_dict = {
    "C": [0.01, 0.1, 10, 100, 200, 500],
    "kernel": ["linear", "rbf", "poly", "sigmoid"]
}

combinations = generate_parameter_combinations(param_dict)
best_combo = None
max_r_score = float('-inf')
dataset = pd.read_csv("insurance_pre.csv")
dataset=pd.get_dummies(dataset,drop_first=True)
independent=dataset[['age', 'bmi', 'children', 'sex_male', 'smoker_yes']]
dependent = dataset[['charges']]
X_train,X_test,y_train,y_test=train_test_split(independent,dependent, test_size=0.30, random_state=0)
data = []

for combo in combinations:
    regressor = make_pipeline(StandardScaler(), SVR(**combo))
    regressor.fit(X_train, y_train)
    y_predict = regressor.predict(X_test)
    r_score = r2_score(y_test, y_predict)
    combo["r_score"] = r_score
    data.append([combo["C"], combo["kernel"], combo["r_score"]])

    if r_score > max_r_score:
        max_r_score = r_score
        best_combo = combo.copy()

print(tabulate(data, headers=["C", "Kernel", "R Score"], tablefmt="grid"))
df = pd.DataFrame(data, columns=["C", "Kernel", "R Score"])
df.to_excel("svm_results.xlsx", index=False)
print("\nBest combination:")

print(f'C={best_combo["C"]}, kernel={best_combo["kernel"]}, r_score={best_combo["r_score"]}')