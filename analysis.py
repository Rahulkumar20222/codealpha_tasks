import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("all_books.csv")

# Clean Price column
# Extract only the numeric part (works even if price contains Â£ or £)
df["Price"] = df["Price"].astype(str).str.extract(r'(\d+\.\d+)')

# Convert to float
df["Price"] = df["Price"].astype(float)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Analysis
print("\nAverage Price:")
print(df["Price"].mean())

print("\nHighest Price:")
print(df["Price"].max())

print("\nLowest Price:")
print(df["Price"].min())

print("\nRating Counts:")
print(df["Rating"].value_counts())

# Most expensive book
print("\nMost Expensive Book:")
print(df.loc[df["Price"].idxmax()])

# Cheapest book
print("\nCheapest Book:")
print(df.loc[df["Price"].idxmin()])

# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=15)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()

# Save chart
plt.savefig("price_distribution.png")

print("\nChart saved as 'price_distribution.png'")

# Show chart
plt.show()