# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 15:11:53 by adtheus           #+#    #+#              #
#    Updated: 2020/01/13 16:18:13 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
num = [0] 

def func(argv, num):
    try:
        num[0] = int(argv)
        print(num)
        return (0)
    except ValueError:
        return (1)

del sys.argv[0]
if func(sys.argv[0], num) or len(sys.argv) != 1 :
    print ("ERROR")
elif num[0] == 0:
    print ("I'm Zero.")
elif num[0] % 2:
    print ("I'm Odd.")
else:
    print ("I'm Even.")
