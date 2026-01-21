# Data Analysis CLI
Basecamp Bootcamp training project for generating and analyzing e-commerce sales data.

# Features 
- Generate 1000 sample e-commerce transactions using Faker library
- Initial data includes: date, product, quantity, price
- Calculate total revenue, average selling price, best-selling product
- Analyze monthly sales trends

# Installations 
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

# Usage 
1. Generate sample data: `python Data/data_generation.py`
2. Analyze the data: `python src/data_analysis.py`

# Dependencies 
- pandas
- numpy
- faker
- tabulate

# File Structure 
 Data/
  - data_generation.py: Generates 1000 sample sales records
  - sample_sales_data.csv: Generated transaction data
src/
  - data_analysis.py: Analyzes sales data and displays metrics