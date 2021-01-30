class Trainer:
    _id = 0

    def __init__(self, name: str):
        self.name = name
        Trainer._id += 1
        self.id = Trainer._id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer._id + 1
