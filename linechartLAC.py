import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initialising filepath
filePath = "LAC - Excel Datasheet - Tarana.xlsx"
df = pd.read_excel(filePath)

# Selected manufacturers for line chart
manufacurers = ["TESLA", "MG", "FORD", "VAUXHALL", "TOYOTA", "KIA"]

# Selected years for line comparison
years = [str(year) for year in range(2015, 2024)]

# Initialising yearly totals
yearlyData = {}

for year in years:
    cols = [col for col in df.columns if str(year) in col]
    df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")
    yearlyData[year] = df.groupby("Make")[cols].sum().sum(axis=1)

# Creating data frame and keeping previously selected manufacturers
trendDF = pd.DataFrame(yearlyData)
trendDF = trendDF.loc[manufacurers]

# Plotting the line graph
plt.figure(figsize=(12,6))

for manufacturer in manufacurers:
    plt.plot(
        years,
        trendDF.loc[manufacturer],
        marker="o",
        label=manufacturer
    )

# Adding labels to line graph
plt.title("Manufacturer Registration Trends (2015 - 2023)")
plt.xlabel("Year")
plt.ylabel("Registrations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()