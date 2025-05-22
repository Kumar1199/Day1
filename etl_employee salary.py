import pandas as pd

# --- Extract ---
# Simulating a read from an Excel file
data = {
    "EmployeeID": [101, 102, 103],
    "Name": ["Ravi", "Anjali", "Manoj"],
    "BaseSalary": [50000, 60000, 55000],
    "Bonus": [5000, 7000, 6000]
}
df = pd.DataFrame(data)

# --- Transform ---
df["TotalSalary"] = df["BaseSalary"] + df["Bonus"]

# --- Load ---
df.to_csv("employee_salaries.csv", index=False)

print("✅ ETL Completed. CSV generated: employee_salaries.csv")
