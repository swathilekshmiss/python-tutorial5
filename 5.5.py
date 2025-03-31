import pandas as pd
df_read = pd.read_excel("data.xlsx", index_col=0)
print(df_read)
