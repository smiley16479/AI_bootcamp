def ft_filter(function_to_apply, list_of_inputs):
	tab = []
	for i in list_of_inputs:
		if function_to_apply(i):
			tab.append(i)
	return tab


number_list = range(-5, 5)
less_than_zero1 = list(filter(lambda x: x < 0, number_list))
less_than_zero2 = ft_filter(lambda x: x < 0, number_list)

print(less_than_zero1)
print(less_than_zero2)
