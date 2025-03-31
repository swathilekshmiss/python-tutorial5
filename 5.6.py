import pandas as pd
csv_data = {
    "SN": [1, 2, 3],
    "Name": ["Linus Torvalds", "Tim Berners-Lee", "Guido van Rossum"],
    "Country": ["Finland", "England", "Netherlands"],
    "Contribution": ["Linux Kernel", "World Wide Web", "Python"],
    "Year": [1991, 1990, 1991]
}
df_csv = pd.DataFrame(csv_data)
df_csv.to_csv("contributors.csv", index=False)