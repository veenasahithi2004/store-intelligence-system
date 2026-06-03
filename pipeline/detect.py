#STEP 2: BUSINESS METRICS 

import pandas as pd

df = pd.read_csv("data/Brigade_Bangalore_10_April_26.csv")

print("STORE ANALYTICS")
print("-" * 40)

#print(f"Total Transactions: {len(df)}")
print("Unique Orders:", df["order_id"].nunique())
print(f"Total Revenue: ₹{df['total_amount'].sum():,.2f}")

avg_basket = df['total_amount'].sum() / len(df)
print(f"Average Basket Value: ₹{avg_basket:,.2f}")

top_brands = (
    df.groupby("brand_name")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 5 Brands:")
print(top_brands.head())

top_categories = (
    df.groupby("sub_category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 5 Categories:")
print(top_categories.head())