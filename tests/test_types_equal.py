from sim import sim


def test_types_equal():
    results = sim(1000, 10,'tests/types_equal.json')
    error_threshold = 0.01

    assert results['Fire']['weights'] - 0.5 < error_threshold
    assert results['Water']['weights'] - 0.5 < error_threshold
    assert results['Grass']['weights'] - 0.5 < error_threshold 

