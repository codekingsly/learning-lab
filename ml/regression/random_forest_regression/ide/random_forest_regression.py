from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from itertools import product
import pandas as pd
from tabulate import tabulate

def generate_parameter_combinations(param_dict):  
    return [dict(zip(param_dict.keys(), combo)) 
            for combo in product(*param_dict.values())]

param_dict = {
    "n_estimators": [50, 100, 150, 200],
    "criterion" : ["squared_error", "absolute_error", "friedman_mse", "poisson"],
    "max_depth": [5, 10, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 3, 5, 10],
    "min_weight_fraction_leaf": [0, 0.05, 0.1],
    "max_features": [0.3, 0.5, 0.7, 1],
    "max_leaf_nodes": [50, 75, 100, None],
    "min_impurity_decrease": [0, 0.01],
    "bootstrap": [True, False],
    # "oob_score": [True, False],
    # "n_jobs": [-1, 4, None],
    # "random_state": [42, None],
    # "verbose": [0, 1],
    # "warm_start": [True, False],
    # "ccp_alpha": [0, 0.01, 0.02, 0.05],
    # "max_samples": [0.5, 0.6, 0.7, 0.8, None],
    # "monotonic_cst": [1, 0, -1]
}

combinations = generate_parameter_combinations(param_dict)
best_combo = None
max_r_score = float('-inf')
dataset = pd.read_csv("insurance_pre.csv")
dataset=pd.get_dummies(dataset,drop_first=True)
independent=dataset[['age', 'bmi', 'children', 'sex_male', 'smoker_yes']]
dependent = dataset['charges']
X_train,X_test,y_train,y_test=train_test_split(independent,dependent, test_size=0.30, random_state=0)
data = []

for combo in combinations:
    regressor = RandomForestRegressor(**combo)
    regressor.fit(X_train,y_train)
    y_predict = regressor.predict(X_test)
    r_score = r2_score(y_test,y_predict)
    combo["r_score"] = r_score
    data.append([combo["n_estimators"], combo["criterion"],combo["max_depth"],
                 combo["min_samples_split"],combo["min_samples_leaf"],
                 combo["min_weight_fraction_leaf"], combo["max_features"], combo["r_score"],
                 combo["max_leaf_nodes"], combo["min_impurity_decrease"], combo["bootstrap"],
                 combo["r_score"]
                ])
    
    #  ,
    #              combo["min_samples_leaf"], combo["min_weight_fraction_leaf"], combo["max_features"], combo["r_score"],
    # combo["max_leaf_nodes"], combo["min_impurity_decrease"], combo["bootstrap"], combo["oob_score"],
    #              combo["n_jobs"], combo["random_state"], combo["verbose"], combo["warm_start"],
    #              combo["ccp_alpha"], combo["max_samples"], combo["monotonic_cst"]
    
    if r_score > max_r_score:
        max_r_score = r_score
        best_combo = combo.copy()

# print(tabulate(data, headers=["n_estimators","criterion","max_depth","min_samples_split","min_samples_leaf","min_weight_fraction_leaf","max_features","max_leaf_nodes","min_impurity_decrease","bootstrap","oob_score","n_jobs","random_state","verbose","warm_start","ccp_alpha","max_samples","monotonic_cst"], tablefmt="grid"))
df = pd.DataFrame(data, columns=["n_estimators","criterion", "max_depth", "min_samples_split","min_samples_leaf","min_weight_fraction_leaf","max_features","max_leaf_nodes","min_impurity_decrease","bootstrap","r_score"])
df.to_excel("random_forest_tree_results.xlsx", index=False)
print("COMPLETED")
# ,"max_depth","min_samples_split","min_samples_leaf","min_weight_fraction_leaf","max_features"
# ,"max_leaf_nodes","min_impurity_decrease","bootstrap","oob_score","n_jobs","random_state","verbose","warm_start","ccp_alpha","max_samples","monotonic_cst"

# print("\nBest combination:")
# print(f'n_estimators={best_combo["n_estimators"]}, criterion={best_combo["criterion"]}, max_depth={best_combo["max_depth"]},r_score={best_combo["r_score"]}')