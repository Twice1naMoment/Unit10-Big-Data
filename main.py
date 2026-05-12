import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# File Path
fp = "LAB Data Excel sheet - Tarana.xls"

# Define File
df = pd.read_excel(fp, sheet_name="Table 16", header=1)

# Coloumns needed for task
b_df = df[['LA_name', 'M_5ACEM', 'F_5ACEM', 'T_5ACEM']].copy()
b_df.columns = ['Local Authority Name', 'Male %', 'Female %', 'Total %']

# Conversion from numeric to string values
for col in ['Male %', 'Female %', 'Total %']:
    b_df[col] = pd.to_numeric(b_df[col], errors='coerce')

# Removal of null values
b_df = b_df.dropna()
print(b_df.head())
print(b_df.shape)


