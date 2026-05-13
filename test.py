import pandas as pd
import matplotlib.pyplot as plt

filePath = "LAB Data Excel Sheet - Tarana.xlsx"
df = pd.read_excel(filePath, sheet_name="My GCSE Data Set")

# Check the raw data BEFORE conversion
print("Column names:", df.columns.tolist())
print("\nFirst 5 rows of 'Total %':")
print(df["Total %"].head(10))
print("\nData type of 'Total %':", df["Total %"].dtype)
print("\nUnique values (first 20):")
print(df["Total %"].unique()[:20])

# Now clean: remove % sign, strip spaces, convert to float
df["Total %"] = df["Total %"].astype(str).str.replace('%', '').str.strip()
df["Total %"] = pd.to_numeric(df["Total %"], errors='coerce')

# Check after cleaning
print("\nAfter cleaning - data type:", df["Total %"].dtype)
print("First 5 cleaned values:")
print(df["Total %"].head(10))
print("Any NaNs?", df["Total %"].isna().sum())

# Drop rows where conversion failed
df = df.dropna(subset=["Total %"])

# Bins and labels
bins = [60, 70, 80, 90, 100]
labels = ['60-69.9', '70-79.9', '80-89.9', '90-99.9']

# Create band column
df["Band"] = pd.cut(df["Total %"], bins=bins, labels=labels, right=False)
freq = df["Band"].value_counts().sort_index()
print("\nFrequency:")
print(freq)

# Plot
plt.figure(figsize=(8,5))
freq.plot(kind="bar")
plt.title("Grouped frequency of total GCSE performance")
plt.xlabel("Performance Band")
plt.ylabel("Number of Local Authorities")
plt.tight_layout()
plt.show()