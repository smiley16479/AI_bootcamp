class Evaluator:
	@staticmethod  
	def zip_evaluate(a, b): # define the static zip_evaluate() function
		if len(a) != len(b):
			return -1
		sum = 0
		for x, y in zip(a, b):
			sum += (len(x) * y)
		return sum

	@staticmethod  
	def enumerate_evaluate(a, b): # same...
		if len(a) != len(b):
			return -1
		sum = 0
		for count, item in enumerate(a):
			sum +=  (len(item) * b[count])
		return sum


print(Evaluator.zip_evaluate(["Le", "Lorem", "Ipsum", "est", "simple"], [1.0, 2.0, 1.0, 4.0, 0.5]))
print(Evaluator.enumerate_evaluate(["Le", "Lorem", "Ipsum", "est", "simple"], [1.0, 2.0, 1.0, 4.0, 0.5]))