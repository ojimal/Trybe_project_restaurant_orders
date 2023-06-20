from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    cheese = Ingredient("queijo provolone")
    flour = Ingredient("farinha")
    invalid = Ingredient("")

    assert cheese.name == "queijo provolone"
    assert cheese is not flour
    assert cheese.restrictions
    assert invalid.name == ""

    assert cheese.__repr__() == "Ingredient('queijo provolone')"
    assert cheese.__hash__() is cheese.__hash__()
    assert cheese.__hash__() != flour.__hash__()
