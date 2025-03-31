import pandas as pd
data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df_dict = pd.DataFrame(data_dict)
print(df_dict)