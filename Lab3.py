import pandas as pd

# Read Excel file
df = pd.read_csv(r'D:\p3.csv')

print("First few rows")
print(df.head())
print("\nSummary statistics")
print(df.describe())

filtered_data = df[df['Age'] > 30]
print("\nFiltered data (Age > 30):")
print(filtered_data)

sorted_data = df.sort_values(by='Salary', ascending=False)
print("\nSorted data (by Salary):")
print(sorted_data)

df['Bonus'] = df['Salary'] * 0.1
print("\nData with new column (Bonus):")
print(df)

df.to_csv('output.csv', index=False)
print("\nData written to output.xlsx")
