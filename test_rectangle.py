from rectangle import rectangle_area

def test_rectangle_area():

    assert rectangle_area(2, 3) == 6
    assert rectangle_area(0, 4) == 0
    assert rectangle_area(5, 5) == 25
