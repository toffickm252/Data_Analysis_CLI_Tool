import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import os
import numpy as np

print("Starting Data loading Process...")
base_dir = os.getcwd()
data_path = os.path.join(base_dir, 'Data', 'sample_sales_data.csv')
# output_path = os.path.join(base_dir, 'data', 'Cleaned_churn_customers_faker.csv')

# Handle potential encoding errors
try:
    customer_df = pd.read_csv(data_path) # read the data from from the path
except FileNotFoundError:
    print(f"Error: File not found at {data_path}. Check your working directory.")
    exit()

print("Data has been successfully loaded.")

# Basic Data Inspection
print(customer_df.head())
print(customer_df.info())
print(customer_df.describe())
print(customer_df.isnull().sum())
print(customer_df.duplicated().sum())

# # Total Revenue Calculation
# customer_df['Selling_Amount'] = customer_df['quantity'] * customer_df['price']
# total_revenue = customer_df['Selling_Amount'].sum()
# print("Total Revenue from sales data: Ghc",total_revenue)
# print("\n")

# # Average Sales Price 
# average_price = customer_df['price'].mean()
# print("Average Sales Price: Ghc", average_price)

# Best Selling Product 
# best_selling_product = customer_df.groupby('product_name')['quantity'].sum().idxmax()
# print("Best Selling Product:", best_selling_product)

# Calculate Total Revenue 
def total_revenue(df):
    df['Selling_Amount'] = df['quantity'] * df['price'] # quantity multiplied by selling price per item
    return df['Selling_Amount'].sum()

# Calculate Average Sales Price 
def average_price(df):
    return df['price'].mean() # average price of all products

# Best Selling Product
def best_selling_product(df):
    return df.groupby('product')['quantity'].sum().idxmax() # product with highest quantity sold

# analyze monthly sales trends
def monthly_sales_trends(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce') # convert date column to datetime
    df['month'] = df['date'].dt.to_period('M') # extract month and year
    monthly_sales = df.groupby('month')['quantity'].sum() # sum quantity sold per month
    return monthly_sales

# Ouput results in formatted way tabular form
print(f"Total Revenue from sales data: Ghc {total_revenue(customer_df):.3f}")
print(f"Average Sales Price: Ghc {average_price(customer_df):.3f}")
print(f"Best Selling Product: {best_selling_product(customer_df)}")
print("\nMonthly Sales Trends:")
print(monthly_sales_trends(customer_df))

# Tabulate monthly sales trends
from tabulate import tabulate

data = [
    ['Total Revenue', f'Ghc {total_revenue(customer_df):.2f}'],
    ['Average Price', f'Ghc {average_price(customer_df):.2f}'],
    ['Best Selling Product', best_selling_product(customer_df)]
]
print(tabulate(data, headers=['Metric', 'Value'], tablefmt='grid'))