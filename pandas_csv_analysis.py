# Pandas CSV Reader & Basic Analysis
import pandas as pd

print("---- Pandas Data Analysis ----")

# 1️⃣ Create Sample Dataset
data = {
    "Name": ["Asha", "Ravi", "John", "Priya", "Sam"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

# Save sample CSV
df.to_csv("students.csv", index=False)

# 2️⃣ Read CSV
df = pd.read_csv("students.csv")

print("\nHead:")
print(df.head())

print("\nTail:")
print(df.tail())

print("\nData Types:")
print(df.dtypes)

# 3️⃣ Summary Statistics
print("\nSummary Statistics:")
print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Min:\n", df.min(numeric_only=True))
print("Max:\n", df.max(numeric_only=True))
print("Count:\n", df.count())

# 4️⃣ Filtering & Column Selection
filtered = df[df["Marks"] > 85]
selected = df[["Name", "Marks"]]

# 5️⃣ Save filtered data
filtered.to_csv("filtered_students.csv", index=False)
selected.to_excel("selected_students.xlsx", index=False)

print("\nTask Completed Successfully!")
