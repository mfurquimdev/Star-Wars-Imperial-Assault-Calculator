from src import AttackSide
from src import DefenseSide
from src import ResultRoll
from src import SurgeOptions
from src.surge import surge_option


class TestSurgeOptions:
    """Test surge options"""

    def test_surge_damage(self):
        roll = AttackSide(damage=1, surge=1, accuracy=0)
        opt = SurgeOptions(damage=1)

        expected_result = ResultRoll(damage=2, surge=0, accuracy=0)

        actual_result = surge_option(roll, opt)

        assert actual_result == expected_result

    def test_surge_accuracy(self):
        roll = AttackSide(damage=0, surge=1, accuracy=1)
        opt = SurgeOptions(accuracy=2)

        expected_result = ResultRoll(damage=0, surge=0, accuracy=3)

        actual_result = surge_option(roll, opt)

        assert actual_result == expected_result

    def test_surge_blast(self):
        roll = AttackSide(damage=1, surge=1, accuracy=1)
        opt = SurgeOptions(blast=2)

        expected_result = ResultRoll(damage=1, surge=0, accuracy=1, blast=2)

        actual_result = surge_option(roll, opt)

        assert actual_result == expected_result
