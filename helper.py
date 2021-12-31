from enum import Enum


TYPES_FILE_NAME = 'types.json'
NUMBER_OF_BATTLES_PER_ROUND = 1000000
NUMBER_OF_ROUNDS = 10


class Type:
    def __init__(self, json):
        self.name = json['name']
        self.immunes = json['immunes']
        self.weaknesses = json['weaknesses']
        self.strengths = json['strengths']

    def __repr__(self) -> str:
        return f'{self.name} is immune to {self.immunes}, weak to {self.weaknesses}, strong to {self.strengths}'


class BattleResult(Enum):
    WIN = 1
    LOSE = -1
    DRAW = 0


def single_type_battle(types_data: dict, p1: Type, p2: Type) -> BattleResult:
    """
    Returns true if p1 wins, false if p2 wins
    If p1 and p2 are equal, then randomly returns True/False

    All of the scenarios
    Pokemon 1 is strong against Pokemon 2, Pokemon 2 cannot attack (immunity) Pokemon 1, WIN
    Pokemon 1 is strong against Pokemon 2, Pokemon 2 is weak against Pokemon 1, WIN
    Pokemon 1 is strong against Pokemon 2, Pokemon 2 is normal against Pokemon 1, WIN
    Pokemon 1 is strong against Pokemon 2, Pokemon 2 is strong against Pokemon 1, DRAW
    Pokemon 1 is normal against Pokemon 2, Pokemon 2 cannot attack (immunity) Pokemon 1, WIN
    Pokemon 1 is normal against Pokemon 2, Pokemon 2 is weak against Pokemon 1, WIN
    Pokemon 1 is normal against Pokemon 2, Pokemon 2 is normal against Pokemon 1, DRAW
    Pokemon 1 is normal against Pokemon 2, Pokemon 2 is strong against Pokemon 1, LOSE
    Pokemon 1 is weak against Pokemon 2, Pokemon 2 cannot attack (immunity) Pokemon 1, WIN
    Pokemon 1 is weak against Pokemon 2, Pokemon 2 is weak against Pokemon 1, DRAW
    Pokemon 1 is weak against Pokemon 2, Pokemon 2 is normal against Pokemon 1, LOSE
    Pokemon 1 is weak against Pokemon 2, Pokemon 2 is strong against Pokemon 1, LOSE
    Pokemon 1 cannot attack (immunity) Pokemon 2, Pokemon 2 cannot attack (immunity) Pokemon 1, DRAW
    Pokemon 1 cannot attack (immunity) Pokemon 2, Pokemon 2 is weak against Pokemon 1, LOSE
    Pokemon 1 cannot attack (immunity) Pokemon 2, Pokemon 2 is normal against Pokemon 1, LOSE
    Pokemon 1 cannot attack (immunity) Pokemon 2, Pokemon 2 is strong against Pokemon 1, LOSE
    """

    p1_attack = __move_strength(types_data, p1, p2)
    p2_attack = __move_strength(types_data, p2, p1)

    if p1_attack == p2_attack:
        return BattleResult.DRAW
    elif p1_attack > p2_attack:
        return BattleResult.WIN
    else:
        return BattleResult.LOSE


def dual_type_battle(types_data: dict, p1: str, p2: str) -> BattleResult:
    # Split the types by the comma
    p1_types = p1.split(',')
    p2_types = p2.split(',')

    assert len(p1_types) == 1 or len(p1_types) == 2
    assert len(p2_types) == 1 or len(p2_types) == 2

    p1_max_move_strength = __dual_type_move_strength(types_data, p1_types, p2_types)
    p2_max_move_strength = __dual_type_move_strength(types_data, p2_types, p1_types)
    if p1_max_move_strength == p2_max_move_strength:
        return BattleResult.DRAW
    elif p1_max_move_strength > p2_max_move_strength:
        return BattleResult.WIN
    else:
        return BattleResult.LOSE


def __dual_type_move_strength(types_data: dict, p1_types: str, p2_types: str) -> BattleResult:
    p1_max_move_strength = 0
    for p1_type in p1_types:
        current_move_strength = 1
        
        for p2_type in p2_types:
            current_move_strength *= __move_strength(types_data, p1_type, p2_type)

        p1_max_move_strength = max(p1_max_move_strength, current_move_strength)
    return p1_max_move_strength


def __move_strength(types_data, p1, p2):
    p1_attack = 1
    if p2 in types_data[p1].immunes:
        p1_attack = 0
    elif p2 in types_data[p1].weaknesses:
        p1_attack = 0.5
    elif p2 in types_data[p1].strengths:
        p1_attack = 2

    return p1_attack
