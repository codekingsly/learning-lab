from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from itertools import product
import pandas as pd
from tabulate import tabulate

def generate_parameter_combinations(param_dict):  
    return [dict(zip(param_dict.keys(), combo)) 
            for combo in product(*param_dict.values())]

param_dict = {
    "criterion": ["squared_error", "friedman_mse", "absolute_error", "poisson"],
    "splitter" : ["best","random"],
    "max_features": ["sqrt", "log2",None]
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
    regressor = DecisionTreeRegressor(**combo)
    regressor.fit(X_train,y_train)
    y_predict = regressor.predict(X_test)
    r_score = r2_score(y_test,y_predict)
    combo["r_score"] = r_score
    data.append([combo["criterion"], combo["splitter"], combo["max_features"], combo["r_score"]])
    
    if r_score > max_r_score:
        max_r_score = r_score
        best_combo = combo.copy()

print(tabulate(data, headers=["criterion", "splitter", "max_features", "R Score"], tablefmt="grid"))
df = pd.DataFrame(data, columns=["criterion", "splitter", "max_features", "R Score"])
df.to_excel("decision_tree_results.xlsx", index=False)

print("\nBest combination:")
print(f'criterion={best_combo["criterion"]}, splitter={best_combo["splitter"]}, max_features={best_combo["max_features"]},r_score={best_combo["r_score"]}')