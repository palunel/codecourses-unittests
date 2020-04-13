from datetime import date


class Sale:

    def calculate_discount(self, customer, amount):
        is_birthday = customer.is_birthday()
        is_pensioner = customer.is_pensioner()
        if amount < 100:
            return 0
        if is_pensioner and is_birthday:
            return amount * max(0.15, 0.1)
        if is_birthday:
            return amount * 0.1
        if is_pensioner:
            return amount * 0.15
        return 0
