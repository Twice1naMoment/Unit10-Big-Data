import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

# Initialising filepath and data frame
filePath = "LAC - Excel Datasheet - Tarana.xlsx"
df = pd.read_excel(filePath)

# 2023 quarter columns
cols2023 = ["2023Q1", "2023Q2", "2023Q3", "2023Q4"]

# Converting column values to numeric
df[cols2023] = df[cols2023].apply(pd.to_numeric, errors='coerce')

# Total 2023 registrations
df["2023 Total"] = df[cols2023].sum(axis=1)

# Group by manufacturer
top10 = df.groupby("Make")["2023 Total"] \
          .sum() \
          .sort_values(ascending=False) \
          .head(10)

# Plotting bar chart
plt.figure(figsize=(12,6))

bars = plt.bar(top10.index, top10.values,
               color="hotpink",
               edgecolor="black")

# Labels
plt.title("Top 10 Manufacturers by 2023 Registrations")
plt.xlabel("Manufacturer")
plt.ylabel("Registrations")

# Rotate labels of manufacturer
plt.xticks(rotation=45)

# Annotations for bars in bar chart
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             yval + 3000,
             f"{int(yval):,}",
             ha='center',
             fontsize=8)

plt.tight_layout()
plt.show()
