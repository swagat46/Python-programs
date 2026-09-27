import pandas as pd

print("=" * 60)
print("PANDAS STUDENT DATA ANALYZER")
print("=" * 60)

# ------------------------------------------------
# 1. CREATE DATA
# ------------------------------------------------

data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": [
        "Amit", "Neha", "Rahul", "Pooja",
        "Kiran", "Sneha", "Akash", "Priya"
    ],
    "Department": [
        "Computer", "Computer", "IT", "IT",
        "Computer", "IT", "Computer", "IT"
    ],
    "Marks": [82, 91, 74, 88, 95, 67, 79, 90]
}

df = pd.DataFrame(data)

print("\n--- Original Data ---")
print(df)

# ------------------------------------------------
# 2. BASIC INFORMATION
# ------------------------------------------------

print("\n--- Head ---")
print(df.head())

print("\n--- Tail ---")
print(df.tail())

print("\n--- Shape ---")
print(df.shape)

print("\n--- Columns ---")
print(df.columns)

print("\n--- Data Information ---")
df.info()

print("\n--- Statistical Description ---")
print(df.describe())

# ------------------------------------------------
# 3. SELECT COLUMN
# ------------------------------------------------

print("\n--- Names ---")
print(df["Name"])

print("\n--- Marks ---")
print(df["Marks"])

# ------------------------------------------------
# 4. FILTERING
# ------------------------------------------------

print("\n--- Students with Marks >= 75 ---")

passed = df[df["Marks"] >= 75]

print(passed)

# ------------------------------------------------
# 5. MULTIPLE CONDITIONS
# ------------------------------------------------

print("\n--- Computer Students with Marks >= 80 ---")

result = df[
    (df["Department"] == "Computer") &
    (df["Marks"] >= 80)
]

print(result)

# ------------------------------------------------
# 6. ADD NEW COLUMN
# ------------------------------------------------

df["Bonus"] = 5

print("\n--- After Adding Bonus ---")
print(df)

# ------------------------------------------------
# 7. CALCULATED COLUMN
# ------------------------------------------------

df["FinalMarks"] = df["Marks"] + df["Bonus"]

print("\n--- Final Marks ---")
print(df)

# ------------------------------------------------
# 8. CREATE GRADE
# ------------------------------------------------

def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "F"


df["Grade"] = df["FinalMarks"].apply(calculate_grade)

print("\n--- Grade Added ---")
print(df)

# ------------------------------------------------
# 9. SORTING
# ------------------------------------------------

print("\n--- Highest to Lowest ---")

sorted_df = df.sort_values(
    "FinalMarks",
    ascending=False
)

print(sorted_df)

# ------------------------------------------------
# 10. DEPARTMENT-WISE AVERAGE
# ------------------------------------------------

print("\n--- Department Average ---")

department_average = df.groupby(
    "Department"
)["FinalMarks"].mean()

print(department_average)

# ------------------------------------------------
# 11. DEPARTMENT-WISE MAXIMUM
# ------------------------------------------------

print("\n--- Department Highest Marks ---")

department_max = df.groupby(
    "Department"
)["FinalMarks"].max()

print(department_max)

# ------------------------------------------------
# 12. DEPARTMENT-WISE MINIMUM
# ------------------------------------------------

print("\n--- Department Lowest Marks ---")

department_min = df.groupby(
    "Department"
)["FinalMarks"].min()

print(department_min)

# ------------------------------------------------
# 13. COUNT STUDENTS
# ------------------------------------------------

print("\n--- Students per Department ---")

count = df.groupby("Department")["Name"].count()

print(count)

# ------------------------------------------------
# 14. TOPPER
# ------------------------------------------------

print("\n--- Topper ---")

topper = df.loc[
    df["FinalMarks"].idxmax()
]

print(topper)

# ------------------------------------------------
# 15. EXPORT CSV
# ------------------------------------------------

df.to_csv(
    "student_analysis.csv",
    index=False
)

print("\nCSV file created successfully!")

print("=" * 60)
print("PROGRAM COMPLETED")
print("=" * 60)