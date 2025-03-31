import pandas as pd
df_students = pd.read_csv("student.csv")
print("Average CGPA:", df_students["CGPA"].mean())
print("Students with CGPA > 9:\n", df_students[df_students["CGPA"] > 9])
print("CSE Students with CGPA > 9:\n", df_students[(df_students["Branch"] == "CSE") & (df_students["CGPA"] > 9)])
print("Student with Maximum CGPA:\n", df_students.loc[df_students["CGPA"].idxmax()])
print("Average CGPA of Each Branch:\n", df_students.groupby("Branch")["CGPA"].mean())
