from foodstuff.math import subtract_two_integers


def test_subtract_two_integers():
    assert subtract_two_integers(5, 3) == 2
    assert subtract_two_integers(10, 4) == 6
    assert subtract_two_integers(0, 0) == 0
    assert subtract_two_integers(-5, -3) == -2
    assert subtract_two_integers(7, 10) == -3