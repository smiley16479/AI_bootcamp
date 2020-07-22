# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 14:29:04 by adtheus           #+#    #+#              #
#    Updated: 2020/01/16 17:48:56 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import *
from time import sleep

cookbook = {
    "sandwitch": {
        "ingredients": ["ham", "bread", "cheese" , "tomatoe"],
        "meal" : "lunch",
        "prep_time" : 10
    },
    "cake": {
        "ingredients": ["flour", "sugar",  "eggs"],
        "meal" : "dessert",
        "prep_time" : 60
     },
     "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : 15
    }
}

def print_recipe(recipe):
    if recipe in cookbook:
        for cle, valeur in cookbook[recipe].items():
            print("{} : {}.".format(cle, valeur))
    else:
        print("wrong recipe name")

def del_recipe(recipe):
    if recipe in cookbook:
        del cookbook[recipe]

def add_recipe(name, ingredients, meal, prep_time):
    if name not in cookbook:
        cookbook[name] = { "ingredients" : ingredients, "meal" : meal, "prep_time" : prep_time} 

def print_cookbook_recipe(cookbook):
    index = 1
    for cle in cookbook.keys():
        print(str(index) + "." + cle)
        index += 1

def user_entry(user_choice):
    if user_choice is 1:
        print("please enter the name of your recipe:\n>>", end='')
        name = input()
        print("please enter its ingredients separated by a spapce:\n>>", end='')
        ingredients = input().split()
        print("please enter this meal type:\n>>", end='')
        meal = input()
        print("please enter its preparation_time:\n>>", end='')
        prep_time = input()
        add_recipe(name, ingredients, meal, prep_time)
        recipe = input()
    elif user_choice is 2:
        print("Which recipe's name do you want to delete ? :\n>>", end='')
        recipe = input()
        del_recipe(recipe)
        recipe = input()
    elif user_choice is 3:
        print("Which recipe's name do you want to display ? :\n>>", end='')
        recipe = input()
        print_recipe(recipe)
        recipe = input()
    elif user_choice is 4:
        print_cookbook_recipe(cookbook)
        recipe = input()

def clear_terminal():
    print(chr(27) + "[2J")

def print_menu():
    print("Please select an option by typing the corresponding number:\n\
1: Add a recipe\n\
2: Delete a recipe\n\
3: Print a recipe\n\
4: Print the cookbook\n\
5: Quit\n>> ", end = '')

def quit_program():
    print("bye ! ")
    exit()

def main():
    user_choice = 0
    while user_choice != 5:
        print_menu()
        user_choice = input()
        if user_choice.isdigit():
            user_choice = int(user_choice)
        if user_choice not in range(1,6):
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
        else:
            clear_terminal()
            user_entry(user_choice)
    quit_program()

if __name__ == "__main__":
    main()
