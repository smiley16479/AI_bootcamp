
class Vector:
	def __init__(self, values):
		try:
			if isinstance(values, list):
				self.values = values
			elif isinstance(values, int):
				self.values = [i for i in range(0, values)]
			elif isinstance(values, tuple):
				self.values = [i for i in range(values[0], values[1])]
			else:
				print(type(values))
				raise TypeError("You're good to read the code source...")
			self.size = len(self.values)
		except TypeError:
			print('An exception flew by!')
			raise

#est-ce que add c'est du += ou du + ? -> j'ai fait du += là...
	def __add__(self, other):
		if not isinstance(other, int):
			raise TypeError("Not an Int")
		return Vector([x + other for x in self.values] )

	def __radd__(self, other):
		if not isinstance(other, int):
			raise TypeError("Not an Int")
		return Vector([x + other for x in self.values])

	def __sub__(self, other):
		if not isinstance(other, int):
			raise TypeError("Not an Int")
		return 
	
	def __rsub__(self, other):
		if not isinstance(other, int):
			raise TypeError("Not an Int")
		return Vector([x - other for x in self.values])

	def __truediv__(self, other):
		if not isinstance(other, int):
			raise TypeError("Not an Int")
		if other != 0:
			return Vector([x / other for x in self.values])

	def __rtruediv__(self, other):
		if not isinstance(other, int):
			raise TypeError("Not an Int")
		if other != 0:
			return Vector([x / other for x in self.values])

	def __mul__(self, other):
		if not isinstance(other, int):
			raise TypeError("Not an Int")
		return Vector([x * other for x in self.values])

	def __rmul__(self, other):
		if not isinstance(other, int):
			raise TypeError("Not an Int")
		return Vector([x * other for x in self.values])

	def __str__(self):
		text = "(Vector " + str(self.values) + ")"
		return text

	def __repr__(self):
		rep = "(Vector " + str(self.values) + ")"
		return rep