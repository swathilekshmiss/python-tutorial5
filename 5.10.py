import pandas as pd
student_data = {
    "RollNo": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Place": ["New York", "Los Angeles", "Chicago"],
    "Mark": [85, 90, 78]
}
df_students = pd.DataFrame(student_data)
df_students.to_csv("stud.csv", index=False)

# Read and display student data
stud_df = pd.read_csv("stud.csv")
print("Student Data:\n", stud_df)

# Set RollNo as index
stud_df.set_index("RollNo", inplace=True)

# Display Name and Mark
print("Name and Mark:\n", stud_df[["Name", "Mark"]])

# Order by Name
print("Ordered by Name:\n", stud_df.sort_values("Name"))

# Order by Mark Descending
print("Ordered by Mark (Descending):\n", stud_df.sort_values("Mark", ascending=False))

# Average, Median, Mode of Marks
print("Average Mark:", stud_df["Mark"].mean())
print("Median Mark:", stud_df["Mark"].median())
print("Mode Mark:", stud_df["Mark"].mode()[0])

# Min & Max Marks
print("Minimum Mark:", stud_df["Mark"].min())
print("Maximum Mark:", stud_df["Mark"].max())

# Variance & Standard Deviation
print("Variance:", stud_df["Mark"].var())
print("Standard Deviation:", stud_df["Mark"].std())

# Histogram of Marks
plt.hist(stud_df["Mark"], bins=5, edgecolor='black')
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.show()

# Remove Place column
stud_df.drop(columns=["Place"], inplace=True)
print("After Removing Place Column:\n", stud_df)