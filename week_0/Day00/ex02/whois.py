# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 15:11:53 by adtheus           #+#    #+#              #
#    Updated: 2020/01/16 17:29:22 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
num = [0] 

def func(argv):
    try:
        num[0] = int(argv)
        return (0)
    except ValueError:
        return (1)

if len(sys.argv[1:]) != 1 or func(sys.argv[1]):
    print ("ERROR")
elif num[0] == 0:
    print ("I'm Zero.")
elif num[0] % 2:
    print ("I'm Odd.")
else:
    print ("I'm Even.")
