import json
import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    # Fetch all cart details for the given user
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Collect all product IDs in a single step
    product_ids = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        try:
            product_ids.extend(json.loads(contents))  # Safely parse JSON
        except json.JSONDecodeError:
            continue  # Skip invalid content entries

    if not product_ids:
        return []

    # Fetch all product details in bulk
    products_in_cart = products.get_products_bulk(product_ids)  # Optimized bulk fetch
    return products_in_cart


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)

    



