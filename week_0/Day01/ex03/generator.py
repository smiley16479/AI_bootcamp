import random

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	if not isinstance(text, str) or option != None \
	or option != "shuffle" or option != "unique" or option != "ordered":
		print("ERROR")
		return "ERROR"
	tab = text.split(sep)
	if option == "shuffle":
		random.shuffle(tab)
	elif option == "unique":
		tab = set(tab)
	elif option == "ordered":
		tab.sort()
	for i in tab:
		yield i
