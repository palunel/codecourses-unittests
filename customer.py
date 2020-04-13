from datetime import date


class Customer:

    def __init__(self, name, birth_date):
        self.birth_date = birth_date
        self.name = name

    def is_birthday(self):
        today = date.today()
        born = self.birth_date
        return today.month == born.month and today.day == born.day

    def is_pensioner(self):
        today = date.today()
        born = self.birth_date
        return self.get_age(born, today) >= 62

    def get_age(self, born, today):
        age = today.year - born.year
        if today.month < born.month or (today.month == born.month and today.day < born.day):
            age = age - 1
        return age
