from collections import Counter
from typing import List
from products import ProductSource


def checkout(product_source: ProductSource, basket: List[str]) -> int:
    product_list = product_source.get_product_list()

    price = workout_price(product_list, basket)
    return price


def workout_price(product_list, basket):
    basket_occurances = Counter(basket)
    price = 0
    for product in product_list:
        if product["Item"] in basket_occurances:
            quantity = basket_occurances[product["Item"]]

            special_offer = product["Special Price"].split(" ")
            quantity_needed_for_offer = int(special_offer[0])
            offer_price = int(special_offer[2])

            if quantity >= quantity_needed_for_offer:
                special_offer = product["Special Price"].split(" ")
                quantity_needed_for_offer = int(special_offer[0])
                offer_price = int(special_offer[2])
                
                number_of_offers = int(quantity / quantity_needed_for_offer)
                price += offer_price * number_of_offers
                remainder_items = quantity % quantity_needed_for_offer
                price += remainder_items * int(product["Unit Price"])
            else:
                price += quantity * int(product["Unit Price"])

    return price
