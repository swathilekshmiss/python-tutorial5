import pandas as pd
student_data = [[10001, "Jack", 76, 88, 76], [10002, "John", 77, 84, 79], [10003, "Alex", 74, 79, 81]]
df_students = pd.DataFrame(student_data, columns=["Reg_no", "Name", "Sub_Mark1", "Sub_Mark2", "Sub_Mark3"])
df_students.to_csv("students.csv", index=False)