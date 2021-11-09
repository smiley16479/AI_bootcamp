# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <adtheus@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 18:49:26 by adtheus           #+#    #+#              #
#    Updated: 2021/11/09 15:57:54 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

def ft_progress(lst):
    start = time.time()
    for i in lst:
        print("ETA: " + '{0:.2f}'.format((time.time() - start) / (i + 1) * len(lst)) + \
        's [ ' + '{0:.2f}'.format(i / len(lst)) + '%]' + ' '\
        '[' + '>'.rjust(int(20 * i / len(lst)), '=').ljust(20 , ' ') + '] ' + \
        str(i) + '/' + str(len(lst)) + \
        ' | elapsed time ' + '{0:.2f}'.format(time.time() - start) + 's'
        , end='\r')
#        if i == len(lst) - 1:
#            print('\n')
        yield i

listy = range(100)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
