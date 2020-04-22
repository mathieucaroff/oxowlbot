from typing import List

from .deck.helpRecipe import HelpRecipeGroup
from .deck.individualOfClassRecipe import IndividualOfClassRecipeGroup
from .deck.knowledgeRecipe import KnowledgeRecipeGroup
from .deck.relationRecipe import RelationRecipeGroup
from .recipe import Recipe


RECIPE_GROUP_LIST = [
    RelationRecipeGroup,
    IndividualOfClassRecipeGroup,
    KnowledgeRecipeGroup,
    HelpRecipeGroup,
]


class RecipeGetter:
    def get(self) -> List[Recipe]:
        return [
            recipe
            for recipeGroup in RECIPE_GROUP_LIST
            for recipe in recipeGroup().createRecipeList()
        ]
