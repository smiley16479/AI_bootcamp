# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <adtheus@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 19:57:43 by adtheus           #+#    #+#              #
#    Updated: 2021/11/09 16:45:44 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import *

class Recipe:
    """Classe définissant une recette  de cuisine caractérisée par :
    - son nom
    - sa difficulte
    - son temps de preparaion
    - ses ingredients
    - sa description(facultative)
    - son type (dessert, plat, entree)"""

    def __init__(self, nom, cooking_level,cooking_time,ingredients, description, recipe_type):
        """Implement a new 'Recipes' object"""
        try :
            if not isinstance(nom, str) or nom == "":
                raise TypeError("Name is not a string")
            if not isinstance(cooking_level, int) or cooking_level < 0:
                raise TypeError("cooking level is not an int")
            if not isinstance(cooking_time, int) or cooking_time < 0:
                raise TypeError("cooking time is not an int")
            if not isinstance(ingredients, list) or len(ingredients) == 0:
                raise TypeError("Ingredients is not a list")
            if not isinstance(description, str):
                raise TypeError("description is not a string")
            if not isinstance(recipe_type, str) or recipe_type not in {"starter", "lunch", "dessert"}:
                raise TypeError("recipe_type is not a existing type")
        except TypeError:
            print('An exception flew by!')
            raise
        self.name = nom
        self.cooking_lvl  = cooking_level
        self.cooking_time = cooking_time
        self.ingredients  = ingredients
        self.description  = description
        self.recipe_type  = recipe_type

    def __str__(self):
        txt = "Dish to prepare: " + self.name + "\n difficulty: " + str(self.cooking_lvl) + "\n cooking_time: " + str(self.cooking_time) + "\n ingredients: " + str(self.ingredients) + "\n description: " + self.description + "\n recipe_type: " + self.recipe_type
        return txt

    def ft_cooking_time(cooking_time):
        pass

    def ft_description(description):
        pass

    def ft_ingredients(ingredients):
        pass
    
    def ft_recipe_type(recipe_type):
        pass
