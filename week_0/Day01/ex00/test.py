from book import Book
from recipe import Recipe

livre = Book("test")
print(livre.recipes_list)


livre.get_recipe_by_name("starter")