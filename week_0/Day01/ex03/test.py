from generator import generator

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
	print(word)
print()

for word in generator(text, sep=" ", option="shuffle"):
	print(word)
print()

for word in generator(1, sep=" ", option="ordered"):
	print(word)
print()
