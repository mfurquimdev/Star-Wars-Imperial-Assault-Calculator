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
        if isinstance(other, AttackSide):
            return AttackSide(
                accuracy=self.accuracy + other.accuracy,
                damage=self.damage + other.damage,
                surge=self.surge + other.surge,
            )
        elif isinstance(other, SurgeOptions):
            return ResultRoll(
                accuracy=self.accuracy + other.accuracy,
                damage=self.damage + other.damage,
                surge=self.surge + other.surge,
            )

    def __sub__(self, other: DefenseSide | SurgeOptions):
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


@dataclass
class SurgeOptions:
    surge: int = -1
    damage: int = 0
    accuracy: int = 0
    pierce: int = 0
    recover: int = 0
    stun: bool = False
    blast: int = 0
    cleave: int = 0


@dataclass(order=True)
class ResultRoll:
    accuracy: int
    damage: int
    surge: int
