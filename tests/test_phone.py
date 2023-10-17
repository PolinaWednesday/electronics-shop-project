
from src.phone import Phone


def test_init():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_repr():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone) == "iPhone 14"
