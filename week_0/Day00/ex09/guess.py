# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 16:59:34 by adtheus           #+#    #+#              #
#    Updated: 2020/01/16 17:10:22 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import sys 

def welcome_msg():
    print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")

def input_num(num_to_guess):
    num = input("What's your guess between 1 and 99?\n>>")
    if num.isdigit():
        if num != num_to_guess:
            print("Too high!") if int(num) > int(num_to_guess) else print("Too low!")
        return (num)
    elif num == "exit" or num == "Exit":
        print("Goodbye!")
        sys.exit()
    else:
        print("This is not a number")
        return("0") 

def win_msg(attemp):
    if attemp == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations, you've got it!\nYou won in ",attemp, " attempts!")

def exception():
    print("The answer to the ultimate question of life, the universe and everything is 42.")

def main():
    num_to_guess = str(random.randrange(1,100))
    welcome_msg()
    num = input_num(num_to_guess)
    attemp = 1
    while num != num_to_guess:
        num = input_num(num_to_guess)
        attemp += 1
    if num_to_guess == "42":
        exception()
    win_msg(attemp)

if __name__ == "__main__":
    main()
