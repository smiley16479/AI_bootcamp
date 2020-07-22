# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 19:13:11 by adtheus           #+#    #+#              #
#    Updated: 2020/01/16 17:51:20 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import *
import string

if len(argv[1:]) != 2:
    print('Too much Argument\n\t Usage: filterwords.py "Hello, my friend" 3')
elif argv[1].isdigit() or not argv[2].isdigit():
    print('ERROR\nUsage: filterwords.py "Hello, my friend" 3')
else:
    word_list = [word for word in ("".join((char if char.isalpha() else " ") for char in argv[1]).split()) if len(word) > int(argv[2])]
    print(word_list)
