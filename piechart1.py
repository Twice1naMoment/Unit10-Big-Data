import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Excel file initialised
filePath = "LAB Data Excel Sheet - Tarana.xlsx"
df = pd.read_excel(filePath, sheet_name="My GCSE Data Set")

# Convert "Total %" column to number values (turning errors to NaN values)
df["Total %"] = df["Total %"].astype(str).str.replace('%', '').str.strip()
df["Total %"] = pd.to_numeric(df["Total %"], errors='coerce')

# Cleans visualisation by dropping rows where conversion have failed
df = df.dropna(subset=["Total %"])

# Defines bins and labels to match excel data
bins = [60, 70, 80, 90, 100]
labels = ['60-69.9', '70-79.9', '80-89.9', '90-99.9']

# Creating the band column
df["Band"] = pd.cut(df["Total %"], bins=bins, labels=labels, right=False)

# Calculates frequency count
freq = df["Band"].value_counts().sort_index()
print(freq)

# Plots the histogram
plt.figure(figsize=(8,5))
plt.pie(freq, labels=freq.index, autopct="%1.1f%%",
        colors=['#FFB6C1', '#FFC0CB', '#FF69B4', '#FF1493'],
        startangle=90)
plt.title("Grouped frequency of total GCSE performance")
plt.xlabel("Performance Band")
plt.ylabel("Number of Local Authorities")
plt.tight_layout()
plt.show()