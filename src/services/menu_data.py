import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        if not source_path or not source_path.endswith('.csv'):
            raise ValueError('Invalid source path')

        self.dishes = set()

        with open(source_path, 'r') as csv_file:
            file_reader = csv.DictReader(csv_file)
            dishes = {}  # dictionary to store all dishes
            for row in file_reader:
                dish_name = row['dish']
                if dish_name not in dishes:
                    dish = Dish(dish_name, float(row['price']))
                    dishes[dish_name] = dish

                ingredient = Ingredient(row['ingredient'])
                recipe_amount = int(row['recipe_amount'])
                dishes[dish_name].add_ingredient_dependency(ingredient,
                                                            recipe_amount)

        self.dishes = dishes.values()  # set dishes as values for the dic
