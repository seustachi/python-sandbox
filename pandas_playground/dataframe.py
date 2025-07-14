import pandas as pd
from scipy import stats

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "George", "Hannah", "Ivy", "Jack"],
    "Age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "New York", "Los Angeles", "Chicago", "Houston", "Miami"],
    "Salary": [60000, 60000, 60000, 60001, 90000000, 60000, 60000, 60000, 60000, 60000]
}

df = pd.DataFrame(data)
print(df)

#print(f"df.head(): {df.head()}")
#print(f"df.tail(): {df.tail()}")
#print(f"df.info(): {df.info()}")
#print(f"df.describe(): {df.describe()}")
#
#print(f"df.index: {df.index}")
#print(f"df.shape: {df.shape}")
#print(f"df.columns: {df.columns.tolist()}")
print(f"df.dtypes: {df.dtypes}")

print(df.Name)

print(f" First row: {df.iloc[0]}")

df["Salary"] = df["Salary"] * 1.1
print(df)

print(f"df.dtypes: {df.dtypes}")

df["Age_Group"] = df["Age"].apply(lambda x: "Young" if x < 30 else "Old")
print(df)

print(f"Salary standard deviation: {df['Salary'].std()}")

print(f"Salary mean: {df['Salary'].mean()}")
df["Salary_Z_Score"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()
print(df)

df["Salary_Z_Score_scipy"] = (stats.zscore(df["Salary"]))
print(df)

#df.to_csv("data/output.csv", index=False)






