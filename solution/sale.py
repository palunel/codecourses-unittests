from datetime import date
from .discount_policy import DiscountPolicy


class Sale:

    def calculate_discount(self, customer):
        policy = DiscountPolicy()
        is_birthday = customer.is_birthday()
        is_pensioner = customer.is_pensioner()
        birthday_discount = is_birthday*policy.birthday_discount
        pensioner_discount = is_pensioner*policy.pensioner_discount
        return max(birthday_discount, pensioner_discount)
