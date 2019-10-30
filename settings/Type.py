from enum import Enum


class Type(Enum):
    FIRE = 1,
    WATER = 2,
    GRASS = 3,
    ELECTRIC = 4,
    GROUND = 5,
    ROCK = 6,
    POISON = 7,
    FIGHTING = 8,
    GHOST = 9,
    NORMAL = 10,
    PSYCHIC = 11,
    ICE = 12,
    FLYING = 13,
    DRAGON = 14,
    BUG = 15,
    DARK = 16,
    STEEL = 17,
    FAIRY = 18


class Effectiveness(Enum):
    Type.FIRE = {
               'advantages': [Type.BUG, Type.GRASS, Type.STEEL, Type.ICE],
               'weaknesses': [Type.ROCK, Type.FIRE, Type.WATER, Type.DRAGON],
               'resistances': [Type.BUG, Type.STEEL, Type.FIRE, Type.GRASS, Type.ICE],
               'vulnerabilities': [Type.GROUND, Type.ROCK, Type.WATER]
           },
    Type.WATER = {
                'advantages': [Type.GROUND, Type.ROCK, Type.FIRE],
                'weaknesses': [Type.WATER, Type.GRASS, Type.DRAGON],
                'resistances': [Type.WATER, Type.STEEL, Type.FIRE, Type.ICE],
                'vulnerabilities': [Type.GRASS, Type.ELECTRIC]
            },
    Type.GRASS = {
                'advantages': [Type.GROUND, Type.ROCK, Type.WATER],
                'weaknesses': [Type.FLYING, Type.GRASS, Type.DRAGON, Type.POISON, Type.BUG, Type.STEEL, Type.FIRE],
                'resistances': [Type.GROUND, Type.WATER, Type.GRASS, Type.ELECTRIC],
                'vulnerabilities': [Type.FLYING, Type.POISON, Type.BUG, Type.FIRE, Type.ICE]
            },
    Type.POISON = {
                 'advantages': [Type.GRASS, Type.FAIRY],
                 'weaknesses': [Type.POISON, Type.GROUND, Type.ROCK, Type.GHOST],
                 'resistances': [Type.FIGHTING, Type.POISON, Type.GRASS],
                 'vulnerabilities': [Type.GROUND, Type.PSYCHIC],
                 'harmlessness': [Type.STEEL],
                 'immunities': [Type.FAIRY]
             },
    Type.ELECTRIC = {
                   'advantages': [Type.FLYING, Type.WATER],
                   'weaknesses': [Type.GRASS, Type.ELECTRIC, Type.DRAGON],
                   'resistances': [Type.FLYING, Type.STEEL, Type.ELECTRIC],
                   'vulnerabilities': [Type.GROUND],
                   'harmlessness': [Type.GROUND]
               },
