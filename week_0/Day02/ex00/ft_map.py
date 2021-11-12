#https://book.pythontips.com/en/latest/map_filter.html
# def ft_map(function_to_apply, list_of_inputs):
# 	tab = []
# 	for i in list_of_inputs:
# 		tab.append(function_to_apply(i))
# 	return tab

# Avec generator (la bonne pour les nouveaux sujets)
def ft_map(function_to_apply, list_of_inputs):
	try:
		some_object_iterator = iter(list_of_inputs)
	except TypeError as te:
		print(list_of_inputs, 'is not iterable')
	for i in list_of_inputs:
		yield function_to_apply(i)

def add_2(x):
	return x + 2


tab1 = list(map(lambda x : x + 2, range(0, 2)))
tab2 = list(ft_map(add_2, range(0, 2)))
tab3 = ft_map(add_2, range(0, 2))

print(tab1)
print(tab2)