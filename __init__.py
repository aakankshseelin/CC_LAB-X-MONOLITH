from products import dao


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> 'Product':
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    products = dao.list_products()
    return [Product.load(product) for product in products]


def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: Product):
    dao.add_product(product._dict_)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id,qty)


