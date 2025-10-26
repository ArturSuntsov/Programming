class Product:
    """
    Класс для продуктов
    """
    def __init__(self, name, price, amount, category):
        """
        шаблон для создания продукта
        :param name: str
        :param price: int
        :param amount: int
        :param category: str
        """
        self.name = name
        self.price = price
        self.amount = amount
        self.category = category

    def info(self):
        """
        Возвращает информацию о продукте
        :return: str
        """
        return f'Продукт: {self.name}, Цена: {self.price}, Количество: {self.amount}, Категория: {self.category}'


class Order:
    """
    Класс для обработки заказа
    """
    def __init__(self, customer, cart_items):
        """
        шаблон для создания заказа
        :param customer: Customer
        :param cart_items: ShoppingCart
        """
        self.customer = customer
        self.cart_items = cart_items.cart_items.copy()

    def find_cost(self):
        """
        Рассчитывает стоимость заказа
        :return: int
        """
        total_sum = sum(product.price * amount for product, amount in self.cart_items)
        return total_sum


class Customer:
    """
    Класс для клиента
    """
    def __init__(self, name):
        """
        шаблон для создания клиента
        :param name: str
        """
        self.name = name
        self.orders = []

    def add_order(self, order):
        """
        Добавляет заказ в историю клиента
        :param order: Order
        :return: None
        """
        self.orders.append(order)

    def check_orders(self):
        """
        Возвращает историю заказов клиента
        :return: str
        """
        if not self.orders:
            return f'Клиент: {self.name}\nЗаказов нет.'
        result = f'Клиент: {self.name}\nЗаказы:'
        for order in self.orders:
            result += f'\n- Сумма: {order.find_cost()} руб.'
        return result


class ShoppingCart:
    """
    Класс для корзины товаров
    """
    def __init__(self):
        """
        шаблон для создания корзины
        """
        self.cart_items = []

    def add_product_to_cart(self, product, amount):
        """
        Добавляет продукт в корзину
        :param product: Product
        :param amount: int
        :return: None
        """
        self.cart_items.append([product, amount])

    def remove_product_from_cart(self, product):
        """
        Удаляет продукт из корзины
        :param product: Product
        :return: None
        """
        self.cart_items = [[prod, amount] for prod, amount in self.cart_items if prod != product]

    def change_amount_product(self, product, new_amount):
        """
        Изменяет количество продукта в корзине
        :param product: Product
        :param new_amount: int
        :return: None
        """
        for i, (prod, amount) in enumerate(self.cart_items):
            if prod == product:
                if new_amount <= 0:
                    self.remove_product_from_cart(product)
                else:
                    self.cart_items[i] = [prod, new_amount]
                break

