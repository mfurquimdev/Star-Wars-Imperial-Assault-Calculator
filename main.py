#!/bin/env python
from __future__ import annotations

from dataclasses import dataclass
from typing import List
from typing import Tuple
from typing import Union


@dataclass
class AttackSide:
    accuracy: int
    damage: int
    surge: int

    def __add__(self, other: AttackSide):
        return AttackSide(
            accuracy=self.accuracy + other.accuracy,
            damage=self.damage + other.damage,
            surge=self.surge + other.surge,
        )

    def __sub__(self, other: DefenseSide):
        return AttackSide(
            accuracy=-1 if other.dodge else self.accuracy,
            damage=self.damage - other.block,
            surge=self.surge - other.evade,
        )


@dataclass
class DefenseSide:
    evade: int
    block: int
    dodge: int


AttackDie = Tuple[
    AttackSide, AttackSide, AttackSide, AttackSide, AttackSide, AttackSide
]
DefenseDie = Tuple[
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


@dataclass
class Armor:
    pass


@dataclass
class Weapon:
    dice: list[Die]


@dataclass
class Accessory:
    pass


@dataclass
class Hero:
    armor: Armor | None
    weapons: tuple[Weapon | None, Weapon | None]
    accessory: tuple[
        Accessory | None,
        Accessory | None,
        Accessory | None,
    ]


def main():
    mak = [BLUE_DIE, BLUE_DIE]
    dummy = [WHITE_DIE]

    all_combinations: list[AttackSide] = []

    (atk1, atk2) = mak
    (def1,) = dummy
    for side1 in atk1:
        for side2 in atk2:
            for side_def1 in def1:
                all_combinations.append(side1 + side2 - side_def1)

    sum_dogde = 0
    for result in all_combinations:
        if result.accuracy == -1:
            sum_dogde += 1

    print(sum_dogde / len(all_combinations))


if __name__ == "__main__":
    main()
