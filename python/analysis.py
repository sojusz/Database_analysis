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


def chart(table, column, width, title, xlabel, ylabel, png_name, chart_name):
    plt.figure(figsize=(width, 6))
    if chart_name == "bar":
        plt.barh(table[column][::-1], table["revenue"][::-1] / 1000, color="skyblue")
    elif chart_name == "basic":
        plt.plot(table.index, table.values, marker="o", color="b", linestyle="-")

    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    if chart_name == "bar":
        plt.grid(axis="x", linestyle="--", alpha=0.6)
        for index, value in enumerate(table["revenue"][::-1] / 1000):
            plt.text(value + 0.5, index, f"${value:.1f}k", va="center", fontsize=9)

        plt.tight_layout()
    elif chart_name == "basic":
        plt.xticks(table.index)
        plt.grid(True, linestyle="--", alpha=0.6)

    chart_to_png(png_name)
    plt.show()


def monthly_revenue_chart():
    orders["orderDate"] = pd.to_datetime(orders["orderDate"])
    df = pd.merge(orders, orderdetails, on="orderNumber")
    df["totalValue"] = df["quantityOrdered"] * df["priceEach"]
    df_2005 = df[df["orderDate"].dt.year == 2005].copy()
    monthly_revenue = df_2005.groupby(df_2005["orderDate"].dt.month)['totalValue'].sum()

    chart(monthly_revenue, "", 10, "Total monthly revenue for 2005", "Month", "Revenue (USD)",
          "monthly_revenue.png", "basic")


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

    chart(top10_products, "productName", 15, "Top 10 products last year", "Revenue (in thousand USD)",
          "Product's name", "top_products.png", "bar")


def categories_revenue_chart():
    orders["orderDate"] = pd.to_datetime(orders["orderDate"])
    last_year = orders["orderDate"].dt.year.max()

    df = pd.merge(orderdetails, orders, on="orderNumber")
    df = pd.merge(df, products, on="productCode")

    df_last_year = df[df["orderDate"].dt.year == last_year].copy()
    df_last_year["revenue"] = df_last_year["quantityOrdered"] * df_last_year["priceEach"]

    categories_list = (
        df_last_year.groupby("productLine")["revenue"]
        .sum().reset_index().sort_values(by="revenue", ascending=False)
    )

    categories_list["share"] = categories_list["revenue"] / categories_list["revenue"].sum() * 100
    print(categories_list)

    chart(categories_list, "productLine", 13, "Categories revenue last year", "Revenue (in thousand USD)",
          "Categories names", "categories_revenue.png", "bar")


def customers_revenue_chart():
    orders["orderDate"] = pd.to_datetime(orders["orderDate"])
    last_year = orders["orderDate"].dt.year.max()

    df = pd.merge(customers, orders, on="customerNumber")
    df = pd.merge(df, orderdetails, on="orderNumber")

    df_last_year = df[df["orderDate"].dt.year == last_year].copy()
    df_last_year["revenue"] = df_last_year["quantityOrdered"] * df_last_year["priceEach"]

    top5_customers = (
        df_last_year.groupby("customerName")["revenue"]
        .sum().reset_index().sort_values(by="revenue", ascending=False).head(5)
    )

    all_rev = df_last_year["revenue"].sum()

    print(top5_customers["revenue"].sum() / all_rev * 100)

    chart(top5_customers, "customerName", 14, "Top 5 customers", "Revenue (in thousand USD)",
          "Client names", "top_customers.png", "bar")

# monthly_revenue_chart()
# top_products_chart()
# categories_revenue_chart()
# customers_revenue_chart()
# df_info(customers)
