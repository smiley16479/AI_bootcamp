# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <adtheus@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 19:21:06 by adtheus           #+#    #+#              #
#    Updated: 2021/11/09 17:20:29 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime 
from recipe import Recipe

class Book:
    """Classe définissant un livre de cuisine caractérisée par :
    - son nom
    - sa date de creation
    - sa date de derniere modification
    - sa liste de recettes"""

    def __init__(self, nom): # Notre méthode constructeur
        """Implement a new 'Book_recipes' object"""
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        self.name = nom
        self.last_update = now 
        self.creation_date = now
        self.recipes_list = {"starter" : set(), "lunch" : set(), "dessert" : set()}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        print("la recette '" + name + "' comporte ces ingredients")
        for val in self.recipes_list.values():
            # print(val)
            for i in val:
                if i.name == name:
                    print(i)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for val in self.recipes_list.keys():
            if val == recipe_type:
                for x in self.recipes_list[val]:
                    print(x)

        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try :
            if str(type(recipe)) != "<class 'recipe.Recipe'>": #print(isinstance(recipe, Recipe))
                raise TypeError("What you added is not a Recipe")
        except TypeError:
            print('An exception flew by!')
            raise
        self.recipes_list[recipe.recipe_type].add(recipe)
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        pass
