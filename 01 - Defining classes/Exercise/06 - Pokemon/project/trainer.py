from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return 'This pokemon is already caught'

        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        pokemon_names = [pokemon.name for pokemon in self.pokemon]
        if pokemon_name not in pokemon_names:
            return 'Pokemon is not caught'

        del self.pokemon[pokemon_names.index(pokemon_name)]
        return f'You have released {pokemon_name}'

    def trainer_data(self):
        trainer_details = [
            f'Pokemon Trainer {self.name}',
            f'Pokemon count {len(self.pokemon)}'
        ]

        pokemon_details = [f'- {pokemon.pokemon_details()}' for pokemon in self.pokemon]

        return '\n'.join(trainer_details + pokemon_details) + '\n'
