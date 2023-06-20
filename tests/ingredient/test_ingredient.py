from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("bacon")
    assert ingredient == ingredient
    ingredient2 = Ingredient("ovo")
    assert ingredient2 != ingredient
    no_ingredient = Ingredient("")
    assert no_ingredient.name == ""

    assert ingredient.restrictions

    assert repr(ingredient) == "Ingredient('bacon')"
    assert hash(ingredient) == hash(ingredient)
    assert hash(ingredient) != hash(ingredient2)
