from src import AttackSide
from src import DefenseSide
from src import ResultRoll
from src import SurgeOptions


def surge_option(roll: AttackSide, opt: SurgeOptions) -> ResultRoll:
    return roll + opt
