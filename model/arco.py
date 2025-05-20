from dataclasses import dataclass

from model.retailer import Retailer


@dataclass
class Arco:
    r1Code: int
    r2Code: int
    peso: int


