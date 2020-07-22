# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 19:21:06 by adtheus           #+#    #+#              #
#    Updated: 2020/01/15 22:03:23 by adtheus          ###   ########.fr        #
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
        self.recipes_list = {"starter", "lunch", "dessert"}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        print("la recette",  name, "comporte ces ingredients")
        print(self.recipes_list[name])

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
