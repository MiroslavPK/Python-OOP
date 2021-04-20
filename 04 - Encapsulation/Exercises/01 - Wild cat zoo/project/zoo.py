class Zoo:
    __budget: float
    __animal_capacity = int
    __workers_capacity = int
    name: str
    animals: list
    workers: list

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

        self.__animals_types = {'Lion': [], 'Tiger': [], 'Cheetah': []}
        self.__workers_types = {'Keeper': [], 'Caretaker': [], 'Vet': []}

    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        animal_type = type(animal).__name__
        self.__animals_types[animal_type].append(animal)

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal_type} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        worker_type = type(worker).__name__
        self.__workers_types[worker_type].append(worker)

        self.workers.append(worker)
        return f"{worker.name} the {worker_type} hired successfully"

    def fire_worker(self, worker_name):
        workers_names = [worker.name for worker in self.workers]
        if worker_name not in workers_names:
            return f"There is no {worker_name} in the zoo"

        worker = self.workers[workers_names.index(worker_name)]
        worker_type = type(worker).__name__
        self.__workers_types[worker_type].remove(worker)

        self.workers.remove(worker)
        self.__workers_capacity += 1
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries_sum = sum([worker.salary for worker in self.workers])
        if salaries_sum > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_tends = sum([animal.get_needs() for animal in self.animals])
        if animals_tends > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_tends
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        for animal_type, animals_per_type in self.__animals_types.items():
            result.append(f"----- {len(animals_per_type)} {animal_type}s:")
            result.append('\n'.join([repr(animal) for animal in animals_per_type]))
        return '\n'.join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        for worker_type, workers_per_type in self.__workers_types.items():
            result.append(f"----- {len(workers_per_type)} {worker_type}s:")
            result.append('\n'.join([repr(worker) for worker in workers_per_type]))
        return '\n'.join(result)
