from __future__ import annotations

from dataclasses import dataclass
from typing import List
from typing import Tuple
from typing import Union


@dataclass(order=True)
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
            damage=max(self.damage - other.block, 0),
            surge=max(self.surge - other.evade, 0),
        )


@dataclass(order=True)
class DefenseSide:
    evade: int
    block: int
    dodge: int
