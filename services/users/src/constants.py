from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


class AddressKind(str, Enum):
    SHIPPING = "shipping"
    BILLING = "billing"
