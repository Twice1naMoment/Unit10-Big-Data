import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initialising filepath and data frame
filePath = "LAC - Excel Datasheet - Tarana.xlsx"
df = pd.read_excel(filePath)

# Cleaning car data and sorting based on quarters
car = df[df["BodyType"] == "Cars"].copy() 
quarters = [c for c in car.columns if c[:4].isdigit()] 
for year in sorted(set(q[:4] for q in quarters)): 
    car[year] = car[[q for q in quarters if q.startswith(year)]].sum(axis=1) 

# Categorises data via their "make" and year
annual = car.groupby("Make")[[str(y) for y in range(2015, 2024)]].sum() 
annual["Total_2015_2023"] = annual.sum(axis=1) 

# Calculating total and annual growth
clean = annual[annual["Total_2015_2023"] >= 10000].copy() 
clean["Growth_2015_2023_%"] = ((clean["2023"] - clean["2015"]) / clean["2015"]) * 100 

print(clean.sort_values("2023", ascending=False).head(10)) 