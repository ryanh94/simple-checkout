from abc import ABC, abstractmethod
import csv
from typing import List


class ProductSource(ABC):
    @abstractmethod
    def get_product_list(self) -> List:
        pass


class ProductsByDict(ProductSource):
    def get_product_list(self) -> List:
        return [
            {"Item": "A", "Unit Price": 50, "Special Price": "3 for 130"},
            {"Item": "B", "Unit Price": 30, "Special Price": "2 for 45"},
            {"Item": "C", "Unit Price": "error", "Special Price": ""},
        ]


class ProductsFromCsv(ProductSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_product_list(self) -> List:
        with open(self.file_path, mode="r") as products:
            reader = csv.DictReader(products, delimiter=";")
            rows = list(reader)

        return rows
