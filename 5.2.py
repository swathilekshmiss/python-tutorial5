import pandas as pd
data = [["Alice", 25], ["Bob", 30], ["Charlie", 35]]
df_list = pd.DataFrame(data, columns=["Name", "Age"], index=[1, 2, 3])
print(df_list)
