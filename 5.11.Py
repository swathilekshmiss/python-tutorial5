import pandas as pd
import matplotlib.pyplot as plt
sales_df = pd.read_csv("sales.csv")

# Scatter Plot - Toothpaste Sales
time = sales_df["month_number"]
toothpaste = sales_df["toothpaste"]
plt.scatter(time, toothpaste)
plt.xlabel("Month")
plt.ylabel("Toothpaste Sales")
plt.title("Toothpaste Sales Data")
plt.show()

# Bar Chart - Face Cream & Face Wash Sales
plt.bar(time, sales_df["facecream"], label="Face Cream")
plt.bar(time, sales_df["facewash"], label="Face Wash", bottom=sales_df["facecream"])
plt.legend()
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Face Cream & Face Wash Sales")
plt.show()

# Pie Chart - Total Sales
sales_df.drop(columns=["month_number"], inplace=True)
sales_df.sum().plot.pie(autopct="%.1f%%")
plt.title("Total Sales Distribution")
plt.show()
