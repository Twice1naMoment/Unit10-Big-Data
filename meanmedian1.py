import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Initialising file path and data frame
filePath = "LAB Data Excel sheet - Tarana.xlsx"
df = pd.read_excel(filePath, sheet_name="My GCSE Data Set")

# Cleaning the data before doing mean and median calculations (through conversion)
df["Total %"] = df["Total %"].astype(str).str.replace("%", "").str.strip()
df["Total %"] = pd.to_numeric(df["Total %"], errors="coerce")

# Dropping values with failed conversions
df = df.dropna(subset=["Total %"])

# Calculating mean and median values
meanVal = df["Total %"].mean()
medianVal = df["Total %"].median()

# Calculating exact mode
modeVals = df["Total %"].mode()
modeExact = modeVals[0] if not modeVals.empty else None

# Print statistical output to console
print(f"Mean = {meanVal:.2f}") # Mean value 
print(f"Median = {medianVal:.2f}") # Median Value
if modeExact is not None: # Checks Mode value and initiases a count for said value
    modeCount = (df["Total %"] == modeExact).sum()
    print(f"Mode = {modeExact} (appears {modeCount} times)")

# Intialising histogram
bins = [60, 70, 80, 90, 100]
plt.figure(figsize=(8,5))
plt.hist(df["Total %"], bins=bins, edgecolor="black", color="hotpink", alpha=0.7)

# Adding mean, median and mode lines to histogram
plt.axvline(meanVal, color="red", linestyle="dashed", linewidth=2, label=f"Mean = {meanVal:.1f}")
plt.axvline(medianVal, color="blue", linestyle="dotted", linewidth=2, label=f"Median = {medianVal:.1f}")
if modeExact is not None:
    plt.axvline(modeExact, color="green", linestyle="dashdot", linewidth=2, label=f"Mode = {modeExact}")

# Adding labels, titles and legend
plt.title("Histogram of GCSE Total % (achieved 5+A*-C) distribution with Mean, Median and Mode ")
plt.xlabel("Total %")
plt.ylabel("Number of Local Authorities")
plt.legend()
plt.tight_layout()
plt.show()
