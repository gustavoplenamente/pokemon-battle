class Pokemon:
    def __init__(self, pokemon_config):
        self.name = pokemon_config['name']
        self.type1 = pokemon_config['type1']
        self.type2 = pokemon_config.get('type2')
        self.moves = pokemon_config['moves']
        self.stats = pokemon_config['stats']
