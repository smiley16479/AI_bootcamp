
class Vector:
	def __init__(self, values):
		try:
			if isinstance(values, list):
				self.values = values
			elif isinstance(values, int) and len(values) == 2:
				self.values = [i for i in range(values[0], values[1])]
			elif isinstance(values, int):
				self.values = [i for i in range(0, values)]
			else:
				raise TypeError("You're good to read the code source...")
		except TypeError:
			print('An exception flew by!')
			raise
		self.size = len(values)

	def __mul__(self, other):
		self.values = [x * other for x in self.values]
		return self

	def __str__(self):
		text = "(Vector " + str(self.values) + ")"
		return text
	