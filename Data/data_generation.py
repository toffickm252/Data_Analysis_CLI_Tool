# Import necessary libraries
# import faker 
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# faker instance 
fake = Faker()

# Product numbers 
records_num = 1000

# Function for sales data 
def Ecommerce_sales(records_num):
    product_list=[
        'Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch',
        'Camera', 'Printer', 'Monitor', 'Keyboard', 'Mouse', 'Speaker',"Smart TV"
    ]

    start_date = datetime.now() - timedelta(days=365)
    data = []

    for i in range(records_num):
        record = {
            "date": fake.date_between(start_date=start_date),  # Random date in past year
            "product": np.random.choice(product_list),          # Pick random product
            "quantity": np.random.randint(1, 11),               # Random 1-10 units
            "price": round(np.random.uniform(10, 500), 2)       # Random price $10-$500
        }
        data.append(record)  # Add to list


        # save data to csv file
    df = pd.DataFrame(data) # Convert list to table
    df.to_csv("Data\\sample_sales_data.csv", index=False)  # Save as CSV file


if __name__ == "__main__":
    Ecommerce_sales(records_num)
        
