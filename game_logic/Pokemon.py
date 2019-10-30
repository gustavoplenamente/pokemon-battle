from game_logic.Move import Move


class Pokemon:
    def __init__(self, pokemon_config):
        self.name = pokemon_config['name']
        self.type1 = pokemon_config['type1']
        self.type2 = pokemon_config.get('type2', None)
        self.moves = pokemon_config['moves']
        self.stats = pokemon_config['stats']
        self.level = pokemon_config.get('level', 5)
        self.types = self.get_types()
        self.selected_move = None
        self._HP = self.stats['HP']

    def get_types(self):
        types = [self.type1]
        types += self.type2 if self.type2 is not None else []
        return types

    def select_move(self, move: Move):
        self.selected_move = move

    def set_HP(self, HP):
        if HP > self.stats['HP']:
            raise ValueError("It is not possible to set a HP value higher than the pokemon's HP stat")
        self._HP = HP if HP > 0 else 0

    def get_HP(self):
        return self._HP
