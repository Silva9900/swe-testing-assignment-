from app import process_input


def test_full_calculation():
    result = process_input(5, "+", 3)
    assert result == 8


def test_clear_function():
    result = process_input(0, "c")
    assert result == 0