#!/bin/env python
from __future__ import annotations

from dataclasses import dataclass
from typing import List
from typing import Tuple
from typing import Union

from src import AttackSide
from src import DefenseSide


@dataclass
class Result:
    accuracy: int
    damage: int
    surge: int
    surge_usages: list[str]


@dataclass
class Armor:
    pass


@dataclass
class Weapon:
    dice: list[AttackDie]


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
    dummy = [BLACK_DIE]

    all_combinations: list[AttackSide] = []

    (atk1, atk2) = mak
    (def1,) = dummy
    for side1 in atk1:
        for side2 in atk2:
            for side_def1 in def1:
                result_side = side1 + side2 - side_def1
                if result_side.surge >= 1:
                    result = Result(
                        accuracy=result_side.accuracy,
                        damage=result_side.damage,
                        surge=result_side.surge - 1,
                        surge_usages=[],
                    )
                all_combinations.append(side1 + side2 - side_def1)

    sum_dogde = 0
    for result in all_combinations:
        if result.surge >= 1:
            sum_dogde += 1

    print(sum_dogde / len(all_combinations))


if __name__ == "__main__":
    main()
