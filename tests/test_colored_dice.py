"""Dice must be exactly this"""
from src import AttackSide
from src import BLACK_DIE
from src import BLUE_DIE
from src import DefenseSide
from src import GREEN_DIE
from src import RED_DIE
from src import WHITE_DIE
from src import YELLOW_DIE


class TestColoredDice:
    """Guarantee the dice are correctly set"""

    def test_red_dice(self):
        assert sorted(RED_DIE) == sorted(
            [
                AttackSide(damage=3, surge=0, accuracy=0),
                AttackSide(damage=1, surge=0, accuracy=0),
                AttackSide(damage=3, surge=0, accuracy=0),
                AttackSide(damage=2, surge=0, accuracy=0),
                AttackSide(damage=2, surge=0, accuracy=0),
                AttackSide(damage=2, surge=1, accuracy=0),
            ]
        )

    def test_yellow_dice(self):
        assert sorted(YELLOW_DIE) == sorted(
            [
                AttackSide(damage=1, surge=0, accuracy=2),
                AttackSide(damage=2, surge=0, accuracy=1),
                AttackSide(damage=0, surge=1, accuracy=0),
                AttackSide(damage=1, surge=2, accuracy=0),
                AttackSide(damage=1, surge=1, accuracy=1),
                AttackSide(damage=0, surge=1, accuracy=2),
            ]
        )

    def test_green_dice(self):
        assert sorted(GREEN_DIE) == sorted(
            [
                AttackSide(damage=1, surge=1, accuracy=2),
                AttackSide(damage=2, surge=0, accuracy=2),
                AttackSide(damage=2, surge=0, accuracy=1),
                AttackSide(damage=1, surge=0, accuracy=3),
                AttackSide(damage=0, surge=1, accuracy=1),
                AttackSide(damage=1, surge=1, accuracy=1),
            ]
        )

    def test_blue_dice(self):
        assert sorted(BLUE_DIE) == sorted(
            [
                AttackSide(damage=1, surge=1, accuracy=3),
                AttackSide(damage=1, surge=0, accuracy=2),
                AttackSide(damage=2, surge=0, accuracy=4),
                AttackSide(damage=2, surge=0, accuracy=3),
                AttackSide(damage=1, surge=0, accuracy=5),
                AttackSide(damage=0, surge=1, accuracy=2),
            ]
        )

    def test_black_dice(self):
        assert sorted(BLACK_DIE) == sorted(
            [
                DefenseSide(block=0, evade=1, dodge=0),
                DefenseSide(block=1, evade=0, dodge=0),
                DefenseSide(block=3, evade=0, dodge=0),
                DefenseSide(block=2, evade=0, dodge=0),
                DefenseSide(block=2, evade=0, dodge=0),
                DefenseSide(block=1, evade=0, dodge=0),
            ]
        )

    def test_white_dice(self):
        assert sorted(WHITE_DIE) == sorted(
            [
                DefenseSide(block=0, evade=0, dodge=0),
                DefenseSide(block=1, evade=0, dodge=0),
                DefenseSide(block=0, evade=1, dodge=0),
                DefenseSide(block=0, evade=0, dodge=1),
                DefenseSide(block=1, evade=1, dodge=0),
                DefenseSide(block=1, evade=1, dodge=0),
            ]
        )
