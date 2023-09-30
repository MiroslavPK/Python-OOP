from .animal import Animal


class Cheetah(Animal):
    def __init__(self, name: str, gender: int, age: int):
        super().__init__(name, gender, age, 60)
