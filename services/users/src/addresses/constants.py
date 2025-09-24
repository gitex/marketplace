from enum import Enum


class AddressKind(str, Enum):
    BILLING = "billing"
    SHIPPING = "shipping"
