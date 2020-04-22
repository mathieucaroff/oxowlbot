from typing import List

from .deck.creatorRecipe import CreatorRecipeGroup
from .deck.helpRecipe import HelpRecipeGroup
from .deck.individualOfClassRecipe import IndividualOfClassRecipeGroup
from .deck.knowledgeRecipe import KnowledgeRecipeGroup
from .deck.relationRecipe import RelationRecipeGroup
from .recipe import Recipe

RECIPE_GROUP_LIST = [
    CreatorRecipeGroup,
    HelpRecipeGroup,
    RelationRecipeGroup,
    IndividualOfClassRecipeGroup,
    KnowledgeRecipeGroup,
]


class RecipeGetter:
    def get(self) -> List[Recipe]:
        return [
            recipe
            for recipeGroup in RECIPE_GROUP_LIST
            for recipe in recipeGroup().createRecipeList()
        ]
