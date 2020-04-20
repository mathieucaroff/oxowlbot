from typing import List

from . import RECIPE_GROUP_LIST
from .recipe import Recipe

class RecipeGetter:
    def get(self) -> List[Recipe]:
        return [
            recipe
            for recipeGroup in RECIPE_GROUP_LIST
            for recipe in recipeGroup().createRecipeList()
        ]
