import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("books.csv")

data["Price"] = data["Price"].str.replace(r"[^0-9.]", "", regex=True)
data["Price"] = data["Price"].astype(float)


print(data.head())

plt.figure(figsize=(10,5))
plt.bar(data["Book Name"][:10], data["Price"][:10])

plt.title("Top 10 Book Prices")
plt.xlabel("Book Name")
plt.ylabel("Price (£)")
plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("book_prices.png")

plt.show()

print("Chart created successfully!")
