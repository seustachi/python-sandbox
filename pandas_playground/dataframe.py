import pandas as pd
from scipy import stats

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "George", "Hannah", "Ivy", "Jack"],
    "Age": [25, 27, 29, 31, 33, 35, 37, 39, 41, 43],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "New York", "Los Angeles", "Chicago", "Houston", "Miami"],
    "Salary": [60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000]
}

df = pd.DataFrame(data)
# print(df)

#print(f"df.head(): {df.head()}")
#print(f"df.tail(): {df.tail()}")
#print(f"df.info(): {df.info()}")
#print(f"df.describe(): {df.describe()}")
#
#print(f"df.index: {df.index}")
#print(f"df.shape: {df.shape}")
#print(f"df.columns: {df.columns.tolist()}")
# print(f"df.dtypes: {df.dtypes}")

# print(df.Name)

# print(f" First row: {df.iloc[0]}")

# df["Salary"] = df["Salary"] * 1.1
# print(df)

# print(f"df.dtypes: {df.dtypes}")

# df["Age_Group"] = df["Age"].apply(lambda x: "Young" if x < 30 else "Old")
# print(df)

# print(f"Salary standard deviation: {df['Salary'].std()}")

# print(f"Salary mean: {df['Salary'].mean()}")
# df["Salary_Z_Score"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()
# print(df)

# df["Salary_Z_Score_scipy"] = (stats.zscore(df["Salary"]))
# print(df)

#df.to_csv("data/output.csv", index=False)

# is_this_a_mask = df["Age"] < 30
# print(is_this_a_mask)

# young_employees = df[df["Age"] < 30]
# print(young_employees)

# young_employees_salary_mean = young_employees["Salary"].mean()
# print(f"Young employees salary mean: {young_employees_salary_mean}")

# young_high_salary_employees = df[(df["Age"] < 30) & (df["Salary"] > 60000)]
# print(young_high_salary_employees)

# specific_cities = df[df["City"].isin(["New York", "Los Angeles"])]
# print(specific_cities)

city_stats = df.groupby("City").agg(
    {"Age": ["mean", "std", "count"],
     "Salary": ["mean", "std", "count"]})

print(city_stats)




