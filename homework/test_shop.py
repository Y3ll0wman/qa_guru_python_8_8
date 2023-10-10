"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity

        # Проверить, что метод возвращает True, когда количество равно запрашиваемому
        assert product.check_quantity(1000) == True

        # Проверить, что метод возвращает True, когда количество больше или равно запрашиваемому
        assert product.check_quantity(0) == True
        assert product.check_quantity(500) == True
        assert product.check_quantity(999) == True

        # Проверить, что метод возвращает False, когда количество меньше запрашиваемого
        assert product.check_quantity(1001) == False
        assert product.check_quantity(1500) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy

        # Купить доступное количество продуктов
        product.buy(500)

        # Проверить, что количество продуктов уменьшилось до 500
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        # Попытка купить больше продуктов, чем доступно - должно вызвать ValueError
        with pytest.raises(ValueError):
            product.buy(1001)

        # Проверить, что количество продукта не изменилось
        assert product.quantity == 1000


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):
        # Добавить продукт в пустую корзину
        cart.add_product(product)

        assert product in cart.products
        assert cart.products[product] == 1

        # Добавить продукта, который уже есть в корзине
        cart.add_product(product, buy_count=2)

        assert cart.products[product] == 3

    def test_remove_product(self, cart, product):
        # Добавить продукт в корзину и удалить его
        cart.add_product(product)
        cart.remove_product(product)

        assert product not in cart.products

        # Добавить два продукта в корзину и удалить один
        cart.add_product(product)
        cart.add_product(product)
        cart.remove_product(product, remove_count=1)

        assert cart.products[product] == 1

    def test_clear(self, cart, product):
        # Добавление продукта и очистка корзины
        cart.add_product(product)
        cart.clear()

        assert not cart.products

    def test_get_total_price(self, cart, product):
        # Рассчитать общую стоимость продуктов в корзине
        cart.add_product(product, buy_count=3)
        total_price = cart.get_total_price()

        assert total_price == 300

    def test_buy(self, cart, product):
        # Совершить покупку
        product.quantity = 5
        cart.add_product(product, buy_count=3)
        cart.buy()

        assert not cart.products
        assert product.quantity == 2

        # Купить продукт, которого нет на складе
        product.quantity = 0
        cart.add_product(product)

        with pytest.raises(ValueError):
            cart.buy()

        # Купить продукт, которого не хватает на складе
        product.quantity = 2
        cart.add_product(product, buy_count=3)

        with pytest.raises(ValueError):
            cart.buy()
