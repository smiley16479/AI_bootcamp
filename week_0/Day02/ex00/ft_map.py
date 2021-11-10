#https://book.pythontips.com/en/latest/map_filter.html
def ft_map(function_to_apply, list_of_inputs):
	tab = []
	for i in list_of_inputs:
		tab.append(function_to_apply(i))
	return tab


def add_2(x):
	return x + 2


tab1 = list(map(lambda x : x + 2, range(0, 2)))
tab2 = ft_map(add_2, range(0, 2))

print(tab1)
print(tab2)