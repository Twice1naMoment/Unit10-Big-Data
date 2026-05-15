import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initialising excel file
filePath = "LAC - Excel Datasheet - Tarana.xlsx"
df = pd.read_excel(filePath)

# Manufacturers to analyse
manufacturers = ["FORD", "TESLA", "MG", "VAUXHALL", "TOYOTA", "KIA"]

# Intialising year range
years = list(range(2015, 2024))

# Dictionary to store yearly totals
manufacturerData = {}

# Creating yearly registration totals
for manufacturer in manufacturers:
    yearlyTotals = []

    for year in years:
        # Select quarter columns for each year
        cols = [col for col in df.columns if str(year) in col]

        # Convert to numeric
        df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

        # Total registrations for manufacturer in that year
        total = df[df["Make"] == manufacturer][cols].sum().sum()
        yearlyTotals.append(total)

    manufacturerData[manufacturer] = yearlyTotals

# Plotting the scatter plot
plt.figure(figsize=(12,7))
for manufacturer in manufacturers:
    y = np.array(manufacturerData[manufacturer])
    x = np.array(years)

    # Initialising the regression line
    slope, intercept = np.polyfit(x, y, 1)
    regression_line = slope * x + intercept

    # Calculating R^2
    correlation_matrix = np.corrcoef(x, y)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2

    # Adding scatter points
    plt.scatter(x, y)

    # Adding the regression line
    plt.plot(
        x,
        regression_line,
        label=f"{manufacturer} | Slope={slope:.0f} | R²={r_squared:.2f}"
    )

    # Print values to console
    print(f"{manufacturer}")
    print(f"Slope = {slope:.2f}")
    print(f"R² = {r_squared:.3f}")
    print()

# Adding labels and titles to scatterplot
plt.title("Regression Analysis of Manufacturer Registrations (2015-2023)")
plt.xlabel("Year")
plt.ylabel("Registrations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()