class DiscountPolicy:

    def __init__(self):
        self.pensioner_discount = 0.15
        self.birthday_discount = 0.1

    @property
    def pensioner_discount(self):
        return self._pensioner_discount

    @pensioner_discount.setter
    def pensioner_discount(self, discount):
        self._pensioner_discount = discount

    @property
    def birthday_discount(self):
        return self._birthday_discount

    @birthday_discount.setter
    def birthday_discount(self, discount):
        self._birthday_discount = discount

