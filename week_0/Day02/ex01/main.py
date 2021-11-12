def what_are_the_vars(*args, **kwargs):
	# print("args len :", len(args))
	# print("kwargs len :", len(kwargs))
	obj = ObjectC()
	nb = 0
	for i in args:
		setattr(obj, "var_" + str(nb), i)
		nb += 1
	for i , j in kwargs.items():
		try :
			if getattr(obj, i):
				return None
		except AttributeError:
			pass
		setattr(obj, str(i), j)
	return obj

class ObjectC(object):
	def __init__(self):
		pass

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)

# New subject
# def what_are_the_vars(...):
# """
# ...
# """
# ... Your code ...
# 
# class ObjectC(object):
	# def __init__(self):
		# pass
# 
	# def doom_printer(obj):
		# if obj is None:
			# print("ERROR")
			# print("end")
			# return
		# for attr in dir(obj):
			# if attr[0] != ’_’:
				# value = getattr(obj, attr)
				# print("{}: {}".format(attr, value))
		# print("end")
# 
# if __name__ == "__main__":
	# obj = what_are_the_vars(7)
	# doom_printer(obj)
	# obj = what_are_the_vars("ft_lol", "Hi")
	# doom_printer(obj)
	# obj = what_are_the_vars()
	# doom_printer(obj)
	# obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	# doom_printer(obj)
	# obj = what_are_the_vars(42, a=10, hello="world")
	# doom_printer(obj)