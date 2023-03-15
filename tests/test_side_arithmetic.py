import pytest

from src import AttackSide
from src import DefenseSide


class TestSideArithmetic:
    """Test side arithmetic"""

    @pytest.mark.parametrize(
        "side1,side2,expected_result",
        [
            (
                AttackSide(damage=1, surge=1, accuracy=0),
                AttackSide(damage=1, surge=0, accuracy=1),
                AttackSide(damage=2, surge=1, accuracy=1),
            ),
            (
                AttackSide(damage=1, surge=0, accuracy=0),
                AttackSide(damage=0, surge=0, accuracy=0),
                AttackSide(damage=1, surge=0, accuracy=0),
            ),
            (
                AttackSide(damage=0, surge=1, accuracy=7),
                AttackSide(damage=0, surge=3, accuracy=8),
                AttackSide(damage=0, surge=4, accuracy=15),
            ),
        ],
    )
    def test_side_addition(self, side1, side2, expected_result):
        actual_result = side1 + side2

        assert actual_result == expected_result

    @pytest.mark.parametrize(
        "side1,side2,expected_result",
        [
            (
                AttackSide(damage=2, surge=0, accuracy=0),
                DefenseSide(block=1, evade=0, dodge=0),
                AttackSide(damage=1, surge=0, accuracy=0),
            ),
            (
                AttackSide(damage=1, surge=0, accuracy=0),
                DefenseSide(block=1, evade=0, dodge=0),
                AttackSide(damage=0, surge=0, accuracy=0),
            ),
            (
                AttackSide(damage=2, surge=0, accuracy=0),
                DefenseSide(block=3, evade=0, dodge=0),
                AttackSide(damage=0, surge=0, accuracy=0),
            ),
            (
                AttackSide(damage=0, surge=1, accuracy=0),
                DefenseSide(block=0, evade=0, dodge=0),
                AttackSide(damage=0, surge=1, accuracy=0),
            ),
            (
                AttackSide(damage=0, surge=1, accuracy=0),
                DefenseSide(block=0, evade=2, dodge=0),
                AttackSide(damage=0, surge=0, accuracy=0),
            ),
            (
                AttackSide(damage=0, surge=0, accuracy=7),
                DefenseSide(block=0, evade=0, dodge=0),
                AttackSide(damage=0, surge=0, accuracy=7),
            ),
            (
                AttackSide(damage=0, surge=0, accuracy=7),
                DefenseSide(block=0, evade=0, dodge=1),
                AttackSide(damage=0, surge=0, accuracy=-1),
            ),
            (
                AttackSide(damage=1, surge=2, accuracy=3),
                DefenseSide(block=2, evade=1, dodge=1),
                AttackSide(damage=0, surge=1, accuracy=-1),
            ),
        ],
    )
    def test_side_subtraction(self, side1, side2, expected_result):
        actual_result = side1 - side2

        assert actual_result == expected_result
