#les decorateur : # https://www.programiz.com/python-programming/decorator

import time
from random import randint
import os

# ... definition of log decorator...
def log(func):
	def inner(self, *arg):
		# print('arg len :', len(arg))
		start = time.time()
		user = os.getenv('USER')
		f = open('machine.log', "a")
		f.write('(' + user + ')Running: ' + func.__name__.ljust(20) + '[ exec-time =' + '{0:.3f}'.format(time.time() - start) + 'ms ]\n')
		ret = func(self) if len(arg) == 0 else func(self, arg[0])
		f.close()
		return ret
	return inner

class CoffeeMachine():
	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":

	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
		
	machine.make_coffee()
	machine.add_water(70)