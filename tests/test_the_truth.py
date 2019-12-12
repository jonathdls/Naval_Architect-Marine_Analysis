"""
Test if the world still make sense
"""


def test_logic():
    """
    GIVEN two logical true statements
    WHEN compared to each other
    THEN check that they are equal
    """
    assert True is True


def test_stability_margin(stability_margin):
    """
    GIVEN a Sevan unit and a semi submersible
    WHEN evaluating stability margins
    THEN check that the Sevan unit has larger margin than a semi
    """

    assert stability_margin('Sevan') > stability_margin('Semi')


def test_cost(cost):
    """
    GIVEN a Sevan FPSO and a ship-shaped FPSO
    WHEN evaluating cost
    THEN check that the Sevan FPSO has lower cost than a ship-shaped FPSO
    """
    assert cost('Sevan FPSO') < cost('Ship-shaped FPSO')
