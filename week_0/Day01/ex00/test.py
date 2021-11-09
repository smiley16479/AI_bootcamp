from book import Book
from recipe import Recipe

livre = Book("test")
#Permet d'avoir sous des type différents des recettes de mm nom
recette1 = Recipe("nom1", 4, 4, ["butter", "oil"] ,"", "lunch")
recette2 = Recipe("nom2", 4, 4, ["margarine"] ,"", "lunch")
recette3 = Recipe("nom2", 4, 4, ["margarine"] ,"", "starter")
recette4 = Recipe("nom2", 4, 4, ["margarine"] ,"", "starter")

livre.add_recipe(recette1)
livre.add_recipe(recette2)
livre.add_recipe(recette3)
livre.add_recipe(recette4)
livre.add_recipe(recette4) #Won't be added twice becose of the set() inside book
livre.add_recipe(4)
livre.get_recipe_by_name("nom1")
print()
livre.get_recipes_by_types("lunch")
print()
livre.get_recipes_by_types("starter")

