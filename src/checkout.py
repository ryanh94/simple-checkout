from collections import Counter
from typing import List
from products import ProductSource


def checkout(product_source: ProductSource, basket: List[str]) -> int:
    product_list = product_source.get_product_list()

    price = workout_price(product_list, basket)
    return price


def workout_price(product_list, basket):
    basket_occurances = Counter(basket)
    total_price = 0
    for product in product_list:
        try:
            if product["Item"] in basket_occurances:
                quantity_in_basket = basket_occurances[product["Item"]]

                special_offer = product["Special Price"].split(" ")
                if special_offer[0] != "" and quantity_in_basket >= int(
                    special_offer[0]
                ):
                    total_price += calculate_special_offer_price(
                        special_offer, quantity_in_basket, int(product["Unit Price"])
                    )
                else:
                    total_price += calculate_no_offer_price(
                        int(product["Unit Price"]), quantity_in_basket
                    )
        except Exception as e:
            # Log error rather than re raise, this would mean that checkout could continue
            raise e

    return total_price


def calculate_special_offer_price(
    special_offer: List, quantity_in_basket: int, unit_price: int
) -> int:
    quantity_needed_for_offer = int(special_offer[0])
    offer_price = int(special_offer[2])

    number_of_offers = int(quantity_in_basket / quantity_needed_for_offer)
    remainder_items = quantity_in_basket % quantity_needed_for_offer

    remainder_price = calculate_no_offer_price(unit_price, remainder_items)

    return (offer_price * number_of_offers) + remainder_price


def calculate_no_offer_price(unit_price: int, quantity: int) -> int:
    return unit_price * quantity
