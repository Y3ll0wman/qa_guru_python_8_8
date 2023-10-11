class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if quantity <= self.quantity:
            return True
        else:
            return False

    def buy(self, quantity_to_buy):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity_to_buy):
            # Если продуктов достаточно, уменьшаем количество в наличии на складе
            self.quantity -= quantity_to_buy

        else:
            raise ValueError(f"Недостаточное количество продукта '{self.name}' для покупки")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """
    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products:
            # Если remove_count не передан или больше или равен количеству в корзине, удалить всю позицию
            if remove_count is None or remove_count >= self.products[product]:
                del self.products[product]
            else:
                # Иначе уменьшаем количество продукта в корзине на указанное значение
                self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        # Проверить, хватает ли продуктов на складе для покупки
        # for product, quantity in self.products.items():
        #     if not product.check_quantity(quantity):
        #         raise ValueError(f"Недостаточное количество продукта '{product.name}' для покупки")
        #
        # # Если все продукты доступны, уменьшить их количество на складе и очистить корзину
        # for product, quantity in self.products.items():
        #     product.quantity -= quantity
        # self.clear()

        for product, quantity in self.products.items():
            product.buy(quantity)

        self.clear()
