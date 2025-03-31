import pandas as pd
car_df = pd.read_csv("auto.csv")

# 1) Clean and Update CSV file
car_df.fillna(method='ffill', inplace=True)
car_df.to_csv("auto_cleaned.csv", index=False)

# 2) Find the most expensive car company
most_expensive_car = car_df.loc[car_df['price'].idxmax()]
print("Most Expensive Car Company:", most_expensive_car['company'])

# 3) Print all Toyota car details
toyota_cars = car_df[car_df['company'].str.lower() == "toyota"]
print("Toyota Cars:\n", toyota_cars)

# 4) Print total cars of all companies
total_cars = car_df['company'].value_counts()
print("Total cars of each company:\n", total_cars)

# 5) Find the highest priced car of all companies
highest_priced_car = car_df.loc[car_df['price'].idxmax()]
print("Highest Priced Car:\n", highest_priced_car)

# 6) Find the average mileage of all companies
avg_mileage = car_df.groupby("company")["average-mileage"].mean()
print("Average Mileage of each company:\n", avg_mileage)

# 7) Sort all cars by Price
sorted_cars = car_df.sort_values(by="price", ascending=False)
print("Cars sorted by price:\n", sorted_cars)
