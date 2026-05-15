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

# Calculating Range, Variance, Standard Deviation and IQR
rangeVal = manTotals.max() - manTotals.min()
varianceVal = manTotals.var()
stdVal = manTotals.std()

# Quartiles
Q1 = manTotals.quantile(0.25)
Q3 = manTotals.quantile(0.75)

# Interquartile Range (IQR)
iqrVal = Q3 - Q1

# Print calculations to console
print("Range =", round(rangeVal, 2))
print("Variance =", round(varianceVal, 2))
print("Standard Deviation =", round(stdVal, 2))
print("IQR =", round(iqrVal, 2))

# Initialising box plot 
plt.figure(figsize=(10,6))

plt.boxplot(
    manTotals,
    vert=True,
    medianprops=dict(color="pink", linewidth=2)
)

plt.title("Dispersion of Manufacturer Registrations")
plt.ylabel("Total Registrations")

plt.show()
