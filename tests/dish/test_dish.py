from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish("lasanha berinjela", 27.00)
    assert dish.name == "lasanha berinjela"
    assert dish.price == 27.00
    dish2 = Dish("lasanha presunto", 35.00)
    assert dish2 != dish
    assert dish2 == dish2

    type_msg = "Dish price must be float."
    with pytest.raises(TypeError, match=type_msg):
        Dish("blabla", "x")
    value_msg = "Dish price must be greater then zero."
    with pytest.raises(ValueError, match=value_msg):
        Dish("blabla", 0)

    assert repr(dish) == "Dish('lasanha berinjela', R$27.00)"
    assert hash(dish) == hash(dish)
    assert hash(dish2) != hash(dish)

    dish2.add_ingredient_dependency(Ingredient("presunto"), 15)
    dish2.add_ingredient_dependency(Ingredient("queijo mussarela"), 15)
    assert dish2.recipe == {
        Ingredient("presunto"): 15,
        Ingredient("queijo mussarela"): 15,
    }

    assert dish2.get_ingredients() == {
        Ingredient("queijo mussarela"),
        Ingredient("presunto"),
    }
    assert dish2.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
