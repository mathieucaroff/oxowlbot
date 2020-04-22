from .deck.knowledgeRecipe import KnowledgeRecipeGroup
from .deck.individualOfClassRecipe import IndividualOfClassRecipeGroup
from .deck.relationRecipe import RelationRecipeGroup
from .deck.helpRecipe import HelpRecipeGroup


RECIPE_GROUP_LIST = [
    RelationRecipeGroup,
    IndividualOfClassRecipeGroup,
    KnowledgeRecipeGroup,
    HelpRecipeGroup,
]
