from typing import List
from .customer import Customer
from .trainer import Trainer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        # subscription info
        subscription = self._get_sub(subscription_id)

        # customer info
        customer_id = subscription.customer_id
        customer = self._get_customer_by_id(customer_id)

        # trainer info
        trainer_id = subscription.trainer_id
        trainer = self._get_trainer_by_id(trainer_id)

        # plans info
        exercise = self._get_exercise_by_id(trainer_id)

        # equipment info
        equipment_id = exercise.equipment_id
        equipment = self._get_equipment_by_id(equipment_id)

        result = [
            repr(subscription),
            repr(customer),
            repr(trainer),
            repr(equipment),
            repr(exercise)
        ]

        return '\n'.join(result)

    def _get_sub(self, subscription_id):
        for sub in self.subscriptions:
            if sub.id == subscription_id:
                return sub

    def _get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def _get_trainer_by_id(self, trainer_id):
        for trainer in self.trainers:
            if trainer.id == trainer_id:
                return trainer

    def _get_exercise_by_id(self, trainer_id):
        for exercise in self.plans:
            if exercise.trainer_id == trainer_id:
                return exercise

    def _get_equipment_by_id(self, equipment_id):
        for equipment in self.equipment:
            if equipment.id == equipment_id:
                return equipment
