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

# Calculating mean for average student performance
meanValue = df["Total %"].mean()
print(f"Mean Total %: {meanValue:.1f}")

# Defines bins and labels to match excel data
bins = [60, 70, 80, 90, 100]
labels = ['60-69.9', '70-79.9', '80-89.9', '90-99.9']

# Initialising histogram
plt.figure(figsize=(8,5))
plt.hist(df["Total %"], bins, edgecolor="black", color="pink", alpha=0.7)

# Adding the mean-line for visualisation
plt.axvline(meanValue, color="red", linestyle="dashed", linewidth="2", label=f"Mean = {meanValue:.1f}")

# Plotting
plt.title("Histogram of GCSE Performance")
plt.xlabel("Total %")
plt.ylabel("Number of Local Authorities")
plt.legend()
plt.tight_layout()
plt.show()