import sys

sys.path.append(".\\src\\")
import pytest
from checkout import checkout
from products import ProductsFromCsv, ProductsByDict


def test_checkout_correct_price():
    product_source = ProductsFromCsv("tests\\unit\\product_list.csv")
    checkout_price = checkout(product_source, ["A", "B", "B"])
    assert checkout_price == 95


def test_checkout_multiple_offers_correct_price():
    product_source = ProductsFromCsv("tests\\unit\\product_list.csv")
    checkout_price = checkout(product_source, ["A", "B", "B", "B", "B", "B"])
    assert checkout_price == 170


def test_checkout_products_from_dictionary_correct_price():
    product_source = ProductsByDict()
    checkout_price = checkout(product_source, ["A", "B", "B", "B", "B", "B"])
    assert checkout_price == 170

    
def test_checkout_invalid_unit_price_rasies_valueError():
    product_source = ProductsByDict()
    with pytest.raises(ValueError):
        checkout(product_source, ["A", "B", "C"])
