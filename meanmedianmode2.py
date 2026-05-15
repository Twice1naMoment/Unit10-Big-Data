import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initialising filepath and data frame
filePath = "LAC - Excel Datasheet - Tarana.xlsx"
df = pd.read_excel(filePath)

# Selecting quarterly columns in excel sheet and converting them to numeric
quarterCol = [
    "2023Q1", "2023Q2", "2023Q3", "2023Q4",
    "2022Q1", "2022Q2", "2022Q3", "2022Q4"
]
df[quarterCol] = df[quarterCol].apply(pd.to_numeric, errors="coerce")

# For Total Registrations column
df["Total Registrations"] = df[quarterCol].sum(axis=1)

# Grouping data by "Make" ans sorts them in descending order
manTotals = df.groupby("Make")["Total Registrations"].sum().sort_values(ascending=False) # "manTotals" stands for manufacturer totals
manTotals = manTotals.head(15)

# Calculations for Mean, Median and Mode
meanVal = manTotals.mean()
medianVal = manTotals.median()

# Print values to console
print("Mean = ", meanVal)
print("Median = ", medianVal)

# Initialising barchart
plt.figure(figsize=(14,7))
plt.bar(manTotals.index, manTotals.values, edgecolor="black", color="lightpink")

# Adding Mean, Median and Mode lines to barchart
plt.axhline(meanVal, color="red", linestyle="dashed", linewidth=2, label=f"Mean = {meanVal:.0f}") 
plt.axhline(medianVal, color="blue", linestyle="dotted", linewidth=2, label=f"Median = {medianVal:.0f}") 

# Adding labels and titles to barchart
plt.title("Barchart of Manufacturer Registrations (Mean, Median averages)")
plt.xlabel("Total Registrations (Make)")
plt.ylabel("Total Registrations")
plt.ticklabel_format(style='plain', axis='y')
plt.legend()
plt.tight_layout()
plt.xticks(rotation=90)

# Show barchart
plt.show()