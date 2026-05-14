import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# File path and data frame generation
filePath = "LAB Data Excel sheet - Tarana.xlsx"
df = pd.read_excel(filePath, sheet_name="My GCSE Data Set")

# Columns for task
b_df = df[['Local Authority Name', 'Male %', 'Female %', 'Total %']].copy()
b_df.columns = ['Local Authority', 'Male', 'Female', 'Total']

# Conversion to numeric in cases any cells were stored as text
for col in ['Male', 'Female', 'Total']:
    b_df[col] = pd.to_numeric(b_df[col], errors='coerce')

# Remove null values
b_df = b_df.dropna()
print(b_df.head())
print(b_df.shape)
