from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
	tab = []
	if len(list_of_inputs) == 1:
		return list_of_inputs[0]
	product = list_of_inputs[0]
	for i in range(len(list_of_inputs)):
		if i == len(list_of_inputs) -1:
			break
		else:
			product += function_to_apply(list_of_inputs[i], list_of_inputs[i + 1])
	return product


print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))
print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))