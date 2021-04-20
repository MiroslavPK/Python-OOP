from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet
from project.zoo import Zoo


zoo = Zoo("Zootopia", 1500, 1, 1)
zoo.hire_worker(Vet("I am Vet", 20, 500))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())


