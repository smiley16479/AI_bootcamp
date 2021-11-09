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
        self.recipes_list = {"starter" : None, "lunch" : None, "dessert" : None}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        print("la recette",  name, "comporte ces ingredients")
        print(self.recipes_list[name])
        # print (str(recipes_list[name.recipe_type][name.name]))

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try :
            if type(recipe) != recipe.Recipe:
                raise TypeError("recipe is not a Recipe")
        except TypeError:
            print('An exception flew by!')
            raise
        recipes_list[recipe.recipe_type].append(recipe)
        pass
