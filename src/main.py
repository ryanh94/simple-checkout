from checkout import checkout
from products import ProductsFromCsv


if __name__ == "__main__":
    product_source = ProductsFromCsv("tests\\unit\\product_list.csv")
    checkout_price = checkout(product_source, ["A", "B", "B"])

    print(f"Chekout price is {checkout_price}")
