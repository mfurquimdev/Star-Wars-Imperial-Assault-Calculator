"""This script describe attack and defense die"""
from .side import AttackSide
from .side import DefenseSide

AttackDie = tuple[
    AttackSide, AttackSide, AttackSide, AttackSide, AttackSide, AttackSide
]
DefenseDie = tuple[
    DefenseSide, DefenseSide, DefenseSide, DefenseSide, DefenseSide, DefenseSide
]


RED_DIE: AttackDie = (
    AttackSide(damage=1, surge=0, accuracy=0),
    AttackSide(damage=3, surge=0, accuracy=0),
    AttackSide(damage=3, surge=0, accuracy=0),
    AttackSide(damage=2, surge=0, accuracy=0),
    AttackSide(damage=2, surge=0, accuracy=0),
    AttackSide(damage=2, surge=1, accuracy=0),
)

YELLOW_DIE: AttackDie = (
    AttackSide(damage=0, surge=1, accuracy=0),
    AttackSide(damage=1, surge=0, accuracy=2),
    AttackSide(damage=2, surge=0, accuracy=1),
    AttackSide(damage=1, surge=2, accuracy=0),
    AttackSide(damage=1, surge=1, accuracy=1),
    AttackSide(damage=0, surge=1, accuracy=2),
)

GREEN_DIE: AttackDie = (
    AttackSide(damage=1, surge=1, accuracy=2),
    AttackSide(damage=2, surge=0, accuracy=2),
    AttackSide(damage=2, surge=0, accuracy=1),
    AttackSide(damage=1, surge=0, accuracy=3),
    AttackSide(damage=0, surge=1, accuracy=1),
    AttackSide(damage=1, surge=1, accuracy=1),
)

BLUE_DIE: AttackDie = (
    AttackSide(damage=1, surge=1, accuracy=3),
    AttackSide(damage=1, surge=0, accuracy=2),
    AttackSide(damage=2, surge=0, accuracy=4),
    AttackSide(damage=2, surge=0, accuracy=3),
    AttackSide(damage=1, surge=0, accuracy=5),
    AttackSide(damage=0, surge=1, accuracy=2),
)

BLACK_DIE: DefenseDie = (
    DefenseSide(block=0, evade=1, dodge=0),
    DefenseSide(block=1, evade=0, dodge=0),
    DefenseSide(block=3, evade=0, dodge=0),
    DefenseSide(block=2, evade=0, dodge=0),
    DefenseSide(block=2, evade=0, dodge=0),
    DefenseSide(block=1, evade=0, dodge=0),
)

WHITE_DIE: DefenseDie = (
    DefenseSide(block=0, evade=0, dodge=0),
    DefenseSide(block=0, evade=0, dodge=1),
    DefenseSide(block=1, evade=0, dodge=0),
    DefenseSide(block=0, evade=1, dodge=0),
    DefenseSide(block=1, evade=1, dodge=0),
    DefenseSide(block=1, evade=1, dodge=0),
)
