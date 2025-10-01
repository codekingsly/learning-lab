import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

# Load
dataset = pd.read_csv('Salary_Data.csv')

independent = dataset[["YearsExperience"]]
dependent = dataset[["Salary"]]

# Split & train
X_train,X_test,y_train,y_test = train_test_split(independent,dependent,test_size=0.3,random_state=0)
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Evaluate
y_pred = regressor.predict(X_test)
r_score = r2_score(y_test,y_pred)

# Save & reload
filename= 'final_model_slr.sav'
pickle.dump(regressor,  open(filename, 'wb'))
load_model = pickle.load(open('final_model_slr.sav', 'rb' ))
result = load_model.predict([[13]])
print("result", result)


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score, mean_absolute_error
# from joblib import dump, load

# def main(csv_path="Salary_Data.csv"):
#     # Load
#     dataset = pd.read_csv(csv_path, usecols=["YearsExperience", "Salary"]).dropna()
#     dataset = dataset.astype({"YearsExperience": "float64", "Salary": "float64"})
#     X = dataset[["YearsExperience"]]
#     y = dataset["Salary"]

#     # Split & train
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#     model = LinearRegression().fit(X_train, y_train)

#     # Evaluate
#     y_pred_test = model.predict(X_test)
#     print("R^2 (test) :", r2_score(y_test, y_pred_test))
#     print("MAE (test) :", mean_absolute_error(y_test, y_pred_test))

#     # Plot
#     plt.figure()
#     plt.scatter(X.values.flatten(), y.values, label="Data")
#     x_sorted = np.sort(X.values.flatten())
#     y_line = model.predict(x_sorted.reshape(-1, 1))
#     plt.plot(x_sorted, y_line, label="Regression Line")
#     plt.xlabel("YearsExperience")
#     plt.ylabel("Salary")
#     plt.title("Simple Linear Regression")
#     plt.legend()
#     plt.show()

#     # Save & reload
#     dump(model, "final_model_slr.joblib")
#     loaded = load("final_model_slr.joblib")
#     new_df = pd.DataFrame({"YearsExperience": [13.0]})
#     pred = loaded.predict(new_df)[0]
#     print("Prediction for 13.0 years:", pred)

#     xmin, xmax = X_train["YearsExperience"].min(), X_train["YearsExperience"].max()
#     if (new_df["YearsExperience"].min() < xmin) or (new_df["YearsExperience"].max() > xmax):
#         print(f"Note: You are extrapolating beyond the training range [{xmin:.2f}, {xmax:.2f}].")

# if __name__ == "__main__":
#     main()
