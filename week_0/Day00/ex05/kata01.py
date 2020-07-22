# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adtheus <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 10:28:19 by adtheus           #+#    #+#              #
#    Updated: 2020/01/14 12:04:18 by adtheus          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/python

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

for n in languages:
    print (n + " was created by "  + languages.get(n))
