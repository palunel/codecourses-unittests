import datetime
from .sale import Sale
from .customer import Customer


class TestSale:

    def test_calculate_discount_customer_not_pensioner_not_birthday_zero_discount(self):
        # Arrange
        customer = customer = Customer("Paul", datetime.datetime(1981, 4, 12))
        sale = Sale()

        # Act
        result = sale.calculate_discount(customer)

        # Assert
        assert result == 0

    def test_calculate_discount_customer_pensioner_not_birthday_pensioner_discount(self):
        customer = customer = Customer("Paul", datetime.datetime(1951, 4, 12))
        sale = Sale()

        result = sale.calculate_discount(customer)

        assert result == 0.15

    def test_calculate_discount_customer_pensioner_birthday_pensioner_discount(self):
        customer = customer = Customer("Paul", datetime.datetime(1951, 4, 13))
        sale = Sale()

        result = sale.calculate_discount(customer)

        assert result == 0.15

    def test_calculate_discount_customer_not_pensioner_birthday_birthday_discount(self):
        customer = customer = Customer("Paul", datetime.datetime(1981, 4, 14))
        sale = Sale()

        result = sale.calculate_discount(customer)

        assert result == 0.1
