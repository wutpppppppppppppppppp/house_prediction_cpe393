import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

DATA_PATH = "Housing.csv"
df = pd.read_csv(DATA_PATH)
print(f'Data is read')
# print(df.head())

# preprocessing
df = df.dropna()
print(f'NaN is dropped')

# encoding
categorical_col = df.select_dtypes(include=["object"]).columns
# print(categorical_col)
lb = LabelEncoder()
for col in categorical_col:
    df[col] = lb.fit_transform(df[col])
print(f'All categorical columns are encoded')
# print(df.info())
# print(df.head())

X, y = df.drop(["price"], axis=1), df["price"]

reg_model = RandomForestRegressor()
reg_model.fit(X,y)
print(f'Model is trained')

with open("app/reg_model.pkl", "wb") as f:
    pickle.dump(reg_model, f)

print(f'Model is saved')