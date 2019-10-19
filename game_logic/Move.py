class Move:
    def __init__(self, move_config):
        self.name = move_config['name'],
        self.type = move_config['type'],
        self.base_power = move_config.get('base_power'),
        self.kind = move_config['category']
