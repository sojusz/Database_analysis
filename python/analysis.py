import pandas as pd
import matplotlib.pyplot as plt
import os

customers = pd.read_csv('C:/Users/wojte/OneDrive/Pulpit/data/customers.csv')
employees = pd.read_csv('C:/Users/wojte/OneDrive/Pulpit/data/employees.csv')
offices = pd.read_csv('C:/Users/wojte/OneDrive/Pulpit/data/offices.csv')
orderdetails = pd.read_csv('C:/Users/wojte/OneDrive/Pulpit/data/orderdetails.csv')
orders = pd.read_csv('C:/Users/wojte/OneDrive/Pulpit/data/orders.csv')
payments = pd.read_csv('C:/Users/wojte/OneDrive/Pulpit/data/payments.csv')
productlines = pd.read_csv('C:/Users/wojte/OneDrive/Pulpit/data/productlines.csv')
products = pd.read_csv('C:/Users/wojte/OneDrive/Pulpit/data/products.csv')


def df_info(df_name):
    print(df_name.info())


def chart_to_png(file_name):
    folder_path = "C:/Users/wojte/OneDrive/Pulpit/charts"
    full_path = os.path.join(folder_path, file_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if os.path.exists(full_path):
        print(f"Ten wykres jest juz zapisany w folderze charts pod nazwa: {file_name}")
    else:
        plt.savefig(full_path, dpi=300, bbox_inches="tight")


def monthly_revenue_chart():
    orders["orderDate"] = pd.to_datetime(orders["orderDate"])
    df = pd.merge(orders, orderdetails, on="orderNumber")
    df["totalValue"] = df["quantityOrdered"] * df["priceEach"]
    df_2005 = df[df["orderDate"].dt.year == 2005].copy()
    monthly_revenue = df_2005.groupby(df_2005["orderDate"].dt.month)['totalValue'].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_revenue.index, monthly_revenue.values, marker="o", color="b", linestyle="-")

    plt.title("Total monthly revenue for 2005", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Revenue (USD)", fontsize=12)

    plt.xticks(monthly_revenue.index)
    plt.grid(True, linestyle="--", alpha=0.6)
    chart_to_png("monthly_revenue.png")
    plt.show()


def top_products_chart():
    orders["orderDate"] = pd.to_datetime(orders["orderDate"])
    last_year = orders["orderDate"].dt.year.max()

    df = pd.merge(orderdetails, products, on="productCode")
    df = pd.merge(df, orders, on="orderNumber")

    df_last_year = df[df["orderDate"].dt.year == last_year].copy()
    df_last_year["revenue"] = df_last_year["quantityOrdered"] * df_last_year["priceEach"]

    top10_products = (
        df_last_year.groupby("productName")["revenue"]
        .sum().reset_index().sort_values(by="revenue", ascending=False).head(10)
    )

    plt.figure(figsize=(15, 6))
    plt.barh(top10_products["productName"][::-1], top10_products["revenue"][::-1] / 1000, color="skyblue")

    plt.title("Top 10 products last year")
    plt.xlabel("Revenue (in thousand USD)", fontsize=12)
    plt.ylabel("Product's name", fontsize=12)
    plt.grid(axis="x", linestyle="--", alpha=0.6)

    for index, value in enumerate(top10_products["revenue"][::-1] / 1000):
        plt.text(value + 0.5, index, f"${value:.1f}k", va="center", fontsize=9)

    plt.tight_layout()
    chart_to_png("top_products.png")
    plt.show()


def categories_revenue_chart():
    orders["orderDate"] = pd.to_datetime(orders["orderDate"])
    last_year = orders["orderDate"].dt.year.max()

    df = pd.merge(orderdetails, orders, on="orderNumber")
    df = pd.merge(df, products, on="productCode")

    df_last_year = df[df["orderDate"].dt.year == last_year].copy()
    df_last_year["revenue"] = df_last_year["quantityOrdered"] * df_last_year["priceEach"]

    categories = (
        df_last_year.groupby(df_last_year["productLine"])["revenue"]
        .sum().reset_index().sort_values(by="revenue", ascending=False)
    )

    plt.figure(figsize=(12, 6))
    plt.barh(categories["productLine"][::-1], categories["revenue"][::-1] / 1000, color="red")

    plt.title("Categories revenue last year")
    plt.xlabel("Revenue (in thousand USD)")
    plt.ylabel("Categories names")
    plt.grid(axis="x", linestyle="--", alpha=0.6)

    for index, value in enumerate(categories["revenue"][::-1] / 1000):
        plt.text(value + 0.5, index, f"${value:.1f}k", va="center", fontsize=9)

    plt.tight_layout()
    chart_to_png("categories_revenue.png")
    plt.show()


# monthly_revenue_chart()
# top_products_chart()
# categories_revenue_chart()
