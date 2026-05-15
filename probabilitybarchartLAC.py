import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initialising file path
filePath = "LAC - Excel Datasheet - Tarana.xlsx"
df = pd.read_excel(filePath)

# Declaring quarter columns
cols2023 = ["2023Q1", "2023Q2", "2023Q3", "2023Q4"]

# Converting values to numeric for calculations
df[cols2023] = df[cols2023].apply(pd.to_numeric, errors='coerce')

# Creating total 2023 registrations
df["2023 Total"] = df[cols2023].sum(axis=1)

# Organising group by manufacturer
manTotals = df.groupby("Make")["2023 Total"].sum()

# Conditional for registration: registrations > 100,000
above100k = (manTotals > 100000).sum()

# Total manufacturers
totalManufacturers = len(manTotals)

# Calculating probability
probability = above100k / totalManufacturers

# Calculating percentage of probability
probPercent = probability * 100

# Print results to console
print(f"Manufacturers above 100,000 = {above100k}")
print(f"Total manufacturers = {totalManufacturers}")
print(f"Probability = {probability:.3f}")
print(f"Percentage = {probPercent:.1f}%")

# Initialising data for bar chart
categories = ["Above 100k", "Below 100k"]
values = [above100k, totalManufacturers - above100k]

# Create bar chart
plt.figure(figsize=(8,6))
bars = plt.bar(categories, values, color=["hotpink", "lightgray"], edgecolor="black")

# Add annotations
for bar in bars:
    yval = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 0.5,
        int(yval),
        ha='center'
    )

# Title and labels
plt.title("Manufacturers Exceeding 100,000 Registrations in 2023")
plt.ylabel("Number of Manufacturers")

# Annotations for probability
plt.figtext(
    0.5,
    -0.05,
    f"P(2023 Registrations > 100,000) = "
    f"{above100k}/{totalManufacturers} = "
    f"{probPercent:.1f}%",
    ha="center",
    fontsize=10
)
plt.tight_layout()
plt.show()