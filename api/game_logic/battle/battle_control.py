import random
import time
from typing import Dict

from game_logic.Player import Player
from settings.EMoveCategory import MoveCategory
from settings.Type import Type, EFFECTIVENESS


class BattleController:
    def __init__(self, players: Dict[Player]):
        self.players = players
        self.pokemon1 = self.players['player1'].pokemon
        self.pokemon2 = self.players['player2'].pokemon
        self.moves_selected = {}

    def start_battle(self):
        # change to battle screen
        self.run_battle()

    def run_battle(self):
        while len(self.moves_selected.keys()) != 2:
            time.sleep(1)

        self.run_moves()

    def run_moves(self):
        if self.pokemon1.stats['Spd'] > self.pokemon2.stats['Spd']:
            self.attack(self.pokemon1, self.pokemon2)
            self.attack(self.pokemon2, self.pokemon1)
        else:
            self.attack(self.pokemon2, self.pokemon1)
            self.attack(self.pokemon1, self.pokemon2)

    def attack(self, attacker, defender):
        move = attacker.selected_move
        damage = self.calculate_damage(attacker, defender, move)
        defender.set_HP(defender.get_HP() - damage)
        if defender.get_HP() == 0:
            self.end_battle(attacker, defender)

    @staticmethod
    def effectiveness(self, pokemon1, pokemon2):
        type_factor = 1
        atk_types = pokemon1.types
        def_types = pokemon2.types
        for atk_type in atk_types:
            for def_type in def_types:
                if def_type in EFFECTIVENESS[atk_type]['advantages']:
                    type_factor *= 2.0
                elif def_type in EFFECTIVENESS[atk_type]['weaknesses']:
                    type_factor *= 0.5
                elif def_type in EFFECTIVENESS[atk_type].get('harmlessness'):
                    type_factor *= 0

        return type_factor

    def calculate_damage(self, attacker, defender, move):
        type_factor = self.effectiveness(attacker, defender)
        stab_factor = 1.5 if move.type in attacker.types else 1
        random_factor = random.randint(84, 100)
        level = attacker.level
        base_power = move.base_power

        if move.category == MoveCategory.SPECIAL:
            attacker_stat = attacker.stats['Sp. Atk']
            defender_stat = defender.stats['Sp. Def']
        elif move.category == MoveCategory.PHYSICAL:
            attacker_stat = attacker.stats['Atk']
            defender_stat = defender.stats['Def']
        else:
            return 0

        base_damage = (((0.4 * level + 2) * attacker_stat * base_power / defender_stat / 50.0) + 2)
        damage = base_damage * stab_factor * type_factor * random_factor // 100

        return damage

    def end_battle(self, winner, loser):
        # Notify winner and loser
        # Suggestion: Erase loser pokemon from battle scene
        # Move to end-battle screen
        pass
