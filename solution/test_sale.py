import datetime
from .sale import Sale
from .customer import Customer


class TestSale:

    def test_calculate_discount_customer_not_pensioner_not_birthday_large_sale_zero_discount(self):
        # Arrange
        customer = customer = Customer("Paul", datetime.datetime(1981, 4, 12))
        sale = Sale()

        # Act
        result = sale.caalculate_discount(customer, 1000)

        # Assert
        assert result == 0

    def test_calculate_discount_small_sale_zero_discount(self):
        customer = customer = Customer("Paul", datetime.datetime(1951, 4, 12))
        sale = Sale()

        result = sale.calculate_discount(customer, 10)

        assert result == 0

    def test_calculate_discount_customer_pensioner_not_birthday_large_sale_pensioner_discount(self):
        customer = customer = Customer("Paul", datetime.datetime(1951, 4, 12))
        sale = Sale()

        result = sale.calculate_discount(customer, 1000)

        assert result == 150

    def test_calculate_discount_customer_pensioner_birthday_large_sale_pensioner_discount(self):
        customer = customer = Customer("Paul", datetime.datetime(1951, 4, 13))
        sale = Sale()

        result = sale.calculate_discount(customer, 1000)

        assert result == 150

    def test_calculate_discount_customer_not_pensioner_birthday_large_sale_birthday_discount(self):
        customer = customer = Customer("Paul", datetime.datetime(1981, 4, 14))
        sale = Sale()

        result = sale.calculate_discount(customer, 1000)

        assert result == 100
