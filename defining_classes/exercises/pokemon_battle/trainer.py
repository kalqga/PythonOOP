class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon_details):
        if pokemon_details not in self.pokemon:
            self.pokemon.append(pokemon_details)
            return f"Caught {pokemon_details.name} with health {pokemon_details.health}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon:
            if pokemon_name == pokemon.name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for pokemon_obj in self.pokemon:
            result += f"- {pokemon_obj.pokemon_details()}\n"
        return result
