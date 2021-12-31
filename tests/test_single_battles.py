from helper import single_type_battle, BattleResult
from sim import load_json_type_data


def test_single_type_battle_simple():
    types = load_json_type_data('tests/types_equal.json')

    result = single_type_battle(types['Fire']['type'], types['Grass']['type'])
    assert result == BattleResult.WIN

    result = single_type_battle(types['Grass']['type'], types['Fire']['type'])
    assert result == BattleResult.LOSE

    result = single_type_battle(types['Water']['type'], types['Water']['type'])
    assert result == BattleResult.DRAW