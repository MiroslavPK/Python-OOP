from typing import List
from .customer import Customer
from .dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        customers_capacity = self.customer_capacity()

        if len(self.customers) < customers_capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        dvd_capacity = self.dvd_capacity()

        if len(self.dvds) < dvd_capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self._find_customer_by_id(customer_id)
        dvd = self._find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self._find_customer_by_id(customer_id)
        dvd = self._find_dvd_by_id(dvd_id)

        if dvd.id not in [dvd.id for dvd in customer.rented_dvds]:
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def _find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def _find_dvd_by_id(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd

    def __repr__(self):
        customers_representation = [customer.__repr__() for customer in self.customers]
        dvds_representation = [dvd.__repr__() for dvd in self.dvds]
        return '\n'.join(customers_representation + dvds_representation)
