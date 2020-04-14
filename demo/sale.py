from datetime import date


class Sale:

    def calculate_discount(self, customer, amount):
        # Business rules:
        # 1. On your birthday you get 10% discount
        # 2. If you are a pensioner (older than 62) you get 15% discount
        # 3. You get maximum of birthday and pensioner discount
        # 4. Discounts only on sales of R100 or more

        # First lets see if it is the customer's birthday
        today = date.today()
        born = customer.birth_date
        if today.month == born.month and today.day == born.day:
            is_birthday = True
        else:
            is_birthday = False

        # Now lets see if the customer is a pensioner
        # First get the age
        if today.month < born.month or (today.month == born.month and today.day < born.day):
            age = today.year - born.year - 1
        else:
            age = today.year - born.year

        # Now see if they are a pensioner
        if age >= 62:
            is_pensioner = True
        else:
            is_pensioner = False

        # Now we can calculate the discount
        discount = 0
        if amount >= 100:
            if is_birthday:
                discount = amount * 0.1
            if is_pensioner:
                discount = amount * 0.15
            if is_pensioner and is_birthday:
                discount = amount * max(0.15, 0.1)

        return discount
