import datetime
from sale import Sale
from customer import Customer

if __name__ == "__main__" :
    customer = Customer("Paul", datetime.datetime(1951, 4, 13))
    sale = Sale()
    sale_amount = 1000
    discount = sale.calculate_discount(customer, sale_amount)
    print(f"{customer.name} received R{discount} discount on their purchase of R{sale_amount} ")
