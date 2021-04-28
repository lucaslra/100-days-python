import pathlib
import sys

import pytest

package_path = pathlib.Path('../')
sys.path.append(str(package_path.resolve()))

from pytesting.groceries import Groceries, Item, DuplicateProduct


def _setup_items():
    products = ['celery', 'apples', 'water', 'coffee', 'chicken', 'pizza']
    prices = [1, 4, 2, 5, 6, 4]
    cravings = False, False, False, False, False, True

    for item in zip(products, prices, cravings):
        yield Item(*item)


@pytest.fixture
def filled_cart():
    items = list(_setup_items())
    return Groceries(items)


def test_initial_empty_cart():
    cart = Groceries()
    assert len(cart) == 0
    assert cart.due == 0


def test_initial_filled_cart(filled_cart):
    assert filled_cart[0].product == 'celery'
    assert filled_cart[0].price == 1
    assert filled_cart[-1].product == 'pizza'
    assert filled_cart[-1].price == 4

    assert len(filled_cart) == 6
    assert filled_cart.due == 22
    assert not filled_cart.num_cravings_reached


def test_add_item(filled_cart):
    oranges = Item(product='oranges', price=3, craving=False)
    filled_cart.add(oranges)

    assert len(filled_cart) == 7
    assert filled_cart[-1].product == 'oranges'
    assert filled_cart[-1].price == 3
    assert filled_cart.due == 25
    assert not filled_cart.num_cravings_reached


def test_add_item_duplicate(filled_cart):
    apples = Item(product='apples', price=4, craving=False)
    with pytest.raises(DuplicateProduct):
        filled_cart.add(apples)
