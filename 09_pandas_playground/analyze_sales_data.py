import pandas as pd
import numpy as np

n = 20

data = {
    "Dates": [f"2024-01-{str(i+1).zfill(2)}" for i in range(n)],
    "Salesperson": ["John", "Jane", "Jim", "Jill", "Jack"] * 4,
    "Quantity": [25, 34, 37, 23, 17, 17, 37, 30, 23, 29, 29, 21, 31, 31, 19, 27, 23, 32, 30, 27],
    "Product": ['Product D', 'Product B', 'Product D', 'Product D', 'Product A', 'Product D', 'Product B', 'Product D', 'Product C', 'Product D', 'Product C', 'Product D', 'Product A', 'Product D', 'Product C', 'Product C', 'Product C', 'Product D', 'Product C', 'Product D'],
    "Price": [109, 143, 210, 246, 312, 97, 153, 202, 246, 308, 110, 144, 201, 246, 304, 98, 153, 201, 246, 308]
}


df = pd.DataFrame(data)
print(df)

total_amount_product_sold = df.groupby("Product").agg({"Quantity": "sum"})
print(total_amount_product_sold)

df["Total_Amount"] = df["Quantity"] * df["Price"]



total_amount_by_product = df.groupby("Product").agg({"Total_Amount": "sum"})
print(total_amount_by_product)

total_amount_by_salesperson = df.groupby("Salesperson").agg({"Total_Amount": "sum"})
print(total_amount_by_salesperson)









