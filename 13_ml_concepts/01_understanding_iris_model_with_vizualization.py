import sklearn
import pandas as pd

from sklearn.datasets import load_iris

import matplotlib.pyplot as plt
import seaborn as sns


iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

print("Iris Dataset Overview:")
print(f"Shape: {df.shape}")
print(f"Features: {list(iris.feature_names)}")
print(f"Species: {list(iris.target_names)}")
print("\nFirst 5 rows:")
print(df.head())

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Sepal measurements
sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', 
                hue='species', ax=axes[0,0])
axes[0,0].set_title('Sepal Measurements')

# 2. Petal measurements  
sns.scatterplot(data=df, x='petal length (cm)', y='petal width (cm)', 
                hue='species', ax=axes[0,1])
axes[0,1].set_title('Petal Measurements')

# 3. Distribution of features
df[iris.feature_names].boxplot(ax=axes[1,0])
axes[1,0].set_title('Feature Distributions')
axes[1,0].tick_params(axis='x', rotation=45)

# 4. Species counts
df['species'].value_counts().plot(kind='bar', ax=axes[1,1])
axes[1,1].set_title('Species Distribution')
axes[1,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()