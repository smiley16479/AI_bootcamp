# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 19:57:43 by adtheus           #+#    #+#              #
#    Updated: 2020/01/15 23:42:15 by adtheus          ###   ########.fr        #
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
        array = []
        array.append( nom if isinstance(nom, str) else print("Name is not a string"))
        array.append( cooking_level if isinstance(cooking_level, int) else print("cooking level is not an int"))
        array.append( cooking_time if isinstance(cooking_time, int)   else print("cooking time is not an int"))
        array.append( ingredients if isinstance(ingredients, list)    else print("Ingredients is not a list"))
        array.append( description if isinstance(description, str)     else print("description is not a string"))
        array.append( recipe_type if isinstance(recipe_type, str)     else print("recipe_type is not a string"))
        if a in array == None:
            print ("something bad")
            exit()
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
