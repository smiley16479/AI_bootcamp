# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 17:46:59 by adtheus           #+#    #+#              #
#    Updated: 2020/01/13 18:19:00 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string

def text_analyzer(strn = ""):
    "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
    tab = [0, 0, 0, 0, 0] 
    if strn == "":
        strn = input("What is the text to analyse?\n>>")
        print(strn)
    for char in strn:
        tab[0] += 1
        if char.isupper():
            tab[1] += 1
        elif char.islower():
            tab[2] += 1
        elif char in string.punctuation:
            tab[3] += 1
        elif char == ' ':
            tab[4] += 1
    print ("The text contains " + str(tab[0]) + " characters:")
    print ("- " + str(tab[1]) + " upper letters")
    print ("- " + str(tab[2]) + " lower letters")
    print ("- " + str(tab[3]) + " punctuation marks")
    print ("- " + str(tab[4]) + " spaces")
