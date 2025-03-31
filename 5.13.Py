import pandas as pd
df = pd.read_csv("employee.csv")
print(df.head(7))
print(df.sort_values("name")["name"])
print(df.loc[df["salary"].idxmax(), "name"])
print(df[df["gender"] == "Male"]["name"])
print(df["team"].unique())